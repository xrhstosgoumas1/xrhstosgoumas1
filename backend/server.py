from fastapi import FastAPI, APIRouter, HTTPException, Request, Response, Depends
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime, timezone, timedelta
import bcrypt
import jwt


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# JWT
JWT_SECRET = os.environ['JWT_SECRET']
JWT_ALGORITHM = "HS256"
TOKEN_EXPIRY_HOURS = 24

# Create the main app without a prefix
app = FastAPI(title="Spider-Man Multiverse API")

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# =====================
# Auth helpers
# =====================
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))


def create_access_token(user_id: str, email: str) -> str:
    payload = {
        "sub": user_id,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=TOKEN_EXPIRY_HOURS),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


async def get_current_user(request: Request) -> dict:
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = auth_header[7:]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = await db.users.find_one({"id": payload["sub"]}, {"_id": 0, "password_hash": 0})
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# =====================
# Auth Models
# =====================
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    name: str = Field(min_length=1, max_length=50)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: str
    name: str


class AuthResponse(BaseModel):
    user: UserResponse
    token: str


# =====================
# Status (existing) Models
# =====================
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StatusCheckCreate(BaseModel):
    client_name: str


# =====================
# Spider-Man Database
# =====================
SPIDERMAN_DB: Dict[str, Any] = {
    "origin": {
        "title": "The Bite That Changed Everything",
        "subtitle": "From Forest Hills to Friendly Neighborhood",
        "paragraphs": [
            "Peter Parker was an unassuming high school student in Queens, New York — bookish, brilliant, and bullied. While attending a public science demonstration on radioactivity, a stray spider, irradiated by experimental beams, descended from above and bit his hand.",
            "That single bite rewrote his DNA. Within hours Peter discovered he could stick to walls, dodge danger before it struck, and lift cars off the ground. Eager to cash in on his gifts, he took the stage as a masked wrestler called 'Spider-Man'.",
            "Then came the night a thief he didn't bother to stop murdered his Uncle Ben. The lesson burned itself into him forever: 'With great power, there must also come great responsibility.' From that moment on, Peter swore his abilities would serve someone other than himself."
        ],
        "quote": "With great power, there must also come great responsibility.",
        "quote_author": "Uncle Ben Parker"
    },
    "powers": [
        {"name": "Wall-Crawling", "icon": "spider", "description": "Peter can adhere to virtually any surface using micro-fibers in his fingertips and feet."},
        {"name": "Spider-Sense", "icon": "radio", "description": "A precognitive tingle warns him of incoming danger milliseconds before it lands."},
        {"name": "Superhuman Strength", "icon": "dumbbell", "description": "He can press over 10 tons, deck the Hulk, and stop a runaway train with two strands of webbing."},
        {"name": "Web-Shooters", "icon": "zap", "description": "Self-engineered wrist devices that fire chemically synthesized webbing of nearly unbreakable tensile strength."},
        {"name": "Reflexes & Agility", "icon": "wind", "description": "Reflexes 40x faster than a normal human; he moves like a hyper-caffeinated acrobat through skyscraper canyons."},
        {"name": "Genius Intellect", "icon": "brain", "description": "Doctorate-level brain in physics, chemistry and engineering — he literally invented his own webbing formula in high school."}
    ],
    "villains": [
        {
            "name": "Green Goblin",
            "real_name": "Norman Osborn",
            "image": "/images/villain-green-goblin.png",
            "threat_level": "OMEGA",
            "description": "Industrialist Norman Osborn dosed himself with an unstable performance serum and emerged as the cackling, glider-riding Green Goblin — Spider-Man's most personal nemesis.",
            "weapon": "Pumpkin Bombs",
            "first_appearance": "The Amazing Spider-Man #14 (July 1964)",
            "affiliations": ["Oscorp Industries", "Sinister Six", "Dark Avengers"],
            "bio": [
                "Norman Osborn was a ruthless industrialist and the cold, calculating father of Peter's best friend, Harry. Driven by an obsession with power and a hunger to outshine his rivals, Osborn experimented on himself with an unstable performance-enhancing serum derived from his stolen formula.",
                "The explosion that followed left him with superhuman strength, accelerated reflexes, and an enhanced — but utterly fractured — intellect. He fashioned a goblin costume, weaponized a personal glider, and unleashed a private war on Spider-Man.",
                "His most unforgivable act came on the George Washington Bridge in 1973, when he murdered Gwen Stacy — a wound Peter Parker has carried for fifty years. Osborn has died, returned, lost his memory, regained it, run the U.S. defense agency H.A.M.M.E.R., and remains the single villain Spider-Man can never truly defeat."
            ]
        },
        {
            "name": "Venom",
            "real_name": "Eddie Brock / Symbiote",
            "image": "/images/villain-venom.png",
            "threat_level": "OMEGA",
            "description": "An alien symbiote bonded to disgraced journalist Eddie Brock, fusing his hatred of Peter with the symbiote's appetite. Immune to Spider-Sense and twice as strong.",
            "weapon": "Symbiote Tendrils",
            "first_appearance": "The Amazing Spider-Man #300 (May 1988)",
            "affiliations": ["Klyntar Symbiote Hive", "Sinister Six", "Lethal Protector"],
            "bio": [
                "Eddie Brock was a rising journalist at the Daily Globe whose career imploded after he wrongly identified the Sin-Eater killer. Spider-Man unmasked the real culprit, Brock's reputation was destroyed, and he blamed Peter Parker for everything.",
                "At the same moment, the alien symbiote Peter had rejected in a church belfry was searching for a new host. The two found each other in that same church — and their shared, white-hot hatred of Spider-Man bonded them instantly.",
                "Venom knows every one of Peter's secrets. The symbiote learned them while bonded to him. Their fights are personal, brutal, and Venom is the one enemy whose attacks Peter's spider-sense cannot detect. Over the decades Eddie has shifted from villain to anti-hero 'Lethal Protector' to outright cosmic guardian — but he remains Spider-Man's ultimate dark mirror."
            ]
        },
        {
            "name": "Doctor Octopus",
            "real_name": "Otto Octavius",
            "image": "/images/villain-doc-ock.png",
            "threat_level": "ALPHA",
            "description": "Brilliant atomic researcher fused to four sentient mechanical arms after a fusion accident. A genius with eight limbs and zero patience.",
            "weapon": "Adamantium-Laced Tentacles",
            "first_appearance": "The Amazing Spider-Man #3 (July 1963)",
            "affiliations": ["Sinister Six (founder)", "Hydra", "Horizon Labs"],
            "bio": [
                "Otto Octavius was a Nobel-caliber atomic researcher whose harness of four mechanically-controlled tentacles allowed him to handle radioactive materials safely — until a lab explosion fused the harness to his spine and his mind.",
                "Reborn as Doctor Octopus, Otto founded the original Sinister Six and tried to defeat Spider-Man in a single coordinated assault. He failed — but the team has hounded Peter ever since.",
                "His most audacious moment came during the 'Superior Spider-Man' arc: dying of a failing body, Otto swapped consciousnesses with Peter Parker and lived as Spider-Man for over a year. He genuinely tried to be a better hero than Peter — and in some ways, succeeded. Peter eventually reclaimed his body, but Otto's bid to BE Spider-Man remains one of the most controversial chapters in the franchise."
            ]
        },
        {
            "name": "Sandman",
            "real_name": "Flint Marko",
            "image": "/images/villain-sandman.png",
            "threat_level": "BETA",
            "description": "Small-time crook caught in a particle test on a beach — now his body IS the beach. He can become a sandstorm or a fifty-foot golem at will.",
            "weapon": "Granular Body Manipulation",
            "first_appearance": "The Amazing Spider-Man #4 (September 1963)",
            "affiliations": ["Sinister Six", "Frightful Four", "Avengers (briefly)"],
            "bio": [
                "William Baker — alias Flint Marko — was a career criminal hiding from the law on a quiet New York beach when a nearby military nuclear test irradiated the sand all around him. His body and the granules fused.",
                "Sandman can shift between solid stone-hard fists, a fine choking sandstorm, or a towering forty-foot golem. He's nearly impossible to permanently knock out — every grain of him has to be contained at once.",
                "Despite his power, Marko has a softer core than most of Spider-Man's enemies. He's a single father trying (and often failing) to do right by his daughter. He has, on occasion, joined the Avengers and even fought alongside Spider-Man — making him one of the rare 'Sinister Six' villains with a real shot at redemption."
            ]
        },
        {
            "name": "Lizard",
            "real_name": "Dr. Curt Connors",
            "image": "/images/villain-lizard.png",
            "threat_level": "ALPHA",
            "description": "Peter's mentor tried to regrow his missing arm with reptilian DNA. He grew it back — and a tail, claws, and a hunger for chaos.",
            "weapon": "Reptilian Mutation",
            "first_appearance": "The Amazing Spider-Man #6 (November 1963)",
            "affiliations": ["Empire State University", "Horizon Labs"],
            "bio": [
                "Dr. Curt Connors was an army surgeon who lost his right arm in combat. Obsessed with the regenerative powers of reptiles, he engineered a serum from lizard DNA — and tested it on himself.",
                "It worked. His arm grew back. Then his teeth sharpened, his skin scaled over, and his mind was overwhelmed by a primal reptilian rage. The Lizard was born.",
                "Connors is one of Spider-Man's most tragic enemies — a brilliant mentor and family man whose monster only emerges when his control slips. Peter has cured him a dozen times. Each time, Curt swears it'll never happen again. Each time, it does."
            ]
        },
        {
            "name": "Mysterio",
            "real_name": "Quentin Beck",
            "image": "/images/villain-mysterio.png",
            "threat_level": "BETA",
            "description": "A washed-up FX artist turned drone-puppeteering illusionist. He doesn't punch you — he convinces you the building you're standing in doesn't exist.",
            "weapon": "Holographic Illusions",
            "first_appearance": "The Amazing Spider-Man #13 (June 1964)",
            "affiliations": ["Sinister Six", "Hollywood (former)"],
            "bio": [
                "Quentin Beck was one of Hollywood's top special-effects artists and stunt designers — until his ego outran his actual talent. Frustrated that 'the people behind the scenes' never get the spotlight, he decided he'd become his own greatest illusion.",
                "Donning a fishbowl helmet filled with hallucinogenic gas and a cape woven from chromatic-spectrum fabric, Mysterio combined practical effects, drone projection, post-hypnotic suggestion and outright stage-magic to convince Spider-Man that the world around him wasn't real.",
                "He's not the strongest villain Peter fights, but he might be the most disorienting. In recent years his illusions have grown sophisticated enough to fool Nick Fury and S.H.I.E.L.D. itself — proving that in the age of deep-fakes, the most dangerous weapon is a really, really convincing lie."
            ]
        }
    ],
    "allies": [
        {
            "name": "Mary Jane Watson",
            "role": "The Love of His Life",
            "image": "/images/ally-mary-jane.png",
            "description": "Actress, model, and the only person who saw Peter Parker before she ever saw the mask.",
            "first_appearance": "The Amazing Spider-Man #25 (June 1965, on-panel #42)",
            "affiliations": ["Daily Bugle (model)", "Broadway", "Stark Industries (briefly)"],
            "bio": [
                "Mary Jane Watson grew up in a broken home with an abusive father, and built her dazzling, world-conquering personality as a defense mechanism. Her famous first line — 'Face it, tiger... you just hit the jackpot' — entered comic history the moment it left her lips.",
                "Behind the bombshell exterior is one of the smartest, toughest characters in the Marvel universe. MJ figured out Peter's secret long before he told her. She didn't just accept it — she chose to stay, knowing exactly what loving Spider-Man would cost her.",
                "Across sixty years of comics, films, and animations, MJ has been Peter's wife, ex-wife, fiancée, best friend, and (in some timelines) the mother of his daughter May 'Mayday' Parker. In every reality, she is his anchor."
            ]
        },
        {
            "name": "Aunt May Parker",
            "role": "Heart of the Family",
            "image": "/images/ally-aunt-may.png",
            "description": "The moral north star who raised Peter. Tougher than every villain on this page combined.",
            "first_appearance": "Amazing Fantasy #15 (August 1962)",
            "affiliations": ["F.E.A.S.T. (homeless shelter, founder)", "Forest Hills, Queens"],
            "bio": [
                "May Reilly Parker raised Peter as her own son after his parents died, and her quiet, unyielding moral strength is the reason Spider-Man exists. Every time Peter has wanted to give up — and there have been many times — May's voice has been the one in his head telling him to get back up.",
                "She has buried a husband, a brother-in-law, and a sister-in-law. She has survived being shot, kidnapped by Doctor Octopus, replaced by a Skrull, and at one point even married Doc Ock himself (long story). She has never broken.",
                "When she discovered Peter's secret, she didn't recoil — she founded F.E.A.S.T., a homeless shelter to give the city's most vulnerable somewhere safe to land. Aunt May is proof that you don't need spider-powers to be a hero."
            ]
        },
        {
            "name": "Miles Morales",
            "role": "The Other Spider-Man",
            "image": "/images/ally-miles-morales.png",
            "description": "Bitten by a different radioactive spider, Miles took up the mantle in his own Brooklyn — and his own universe.",
            "first_appearance": "Ultimate Fallout #4 (August 2011)",
            "affiliations": ["Champions", "Spider-Society", "Brooklyn Visions Academy"],
            "bio": [
                "Miles Gonzalo Morales is the half-Black, half-Puerto Rican son of a former criminal turned cop. A genetically-modified spider — engineered by Oscorp from the same project that created the original — escaped, hitched a ride in his uncle's bag, and bit him.",
                "Unlike Peter, Miles got TWO bonus powers: 'Venom Strike' (a paralyzing electric shock through his hands) and full invisibility / camouflage. He spent years as a Brooklyn-based Spider-Man before the multiverse merged him into the main Marvel reality.",
                "Miles made his pop-culture leap with the Oscar-winning 'Into the Spider-Verse' (2018) and 'Across the Spider-Verse' (2023). He's the proof of Peter's promise: anyone — anywhere — can wear the mask."
            ]
        },
        {
            "name": "Gwen Stacy",
            "role": "First Love / Spider-Woman",
            "image": "/images/ally-gwen-stacy.png",
            "description": "Brilliant, fearless, and in some universes she's the one wearing the suit. In every universe, she matters.",
            "first_appearance": "The Amazing Spider-Man #31 (December 1965)",
            "affiliations": ["Empire State University", "Spider-Society (Earth-65)"],
            "bio": [
                "Gwendolyne Maxine Stacy was Peter's first true love — a brilliant biochemistry student and the daughter of NYPD captain George Stacy. Her death at the Green Goblin's hands on the George Washington Bridge in The Amazing Spider-Man #121 (1973) ended the Silver Age of comics overnight.",
                "For decades, Gwen's death defined what 'losing someone' meant in superhero stories. Her shadow has haunted Peter Parker, Norman Osborn, and Marvel itself.",
                "In 2014, the alternate-reality 'Spider-Gwen' (Earth-65) gave fans the Gwen Stacy who got bitten instead of Peter — a punk-rock drummer turned Spider-Woman in white-and-pink. She has since become one of the most popular characters in the entire Spider-franchise."
            ]
        },
        {
            "name": "Ned Leeds",
            "role": "The Guy in the Chair",
            "image": "/images/ally-ned-leeds.png",
            "description": "Peter's best friend and unofficial mission-control. Knows the secret. Tells nobody.",
            "first_appearance": "The Amazing Spider-Man #18 (November 1964) — modern MCU version, Captain America: Civil War (2016)",
            "affiliations": ["Midtown School of Science and Technology", "Daily Bugle (comics)"],
            "bio": [
                "In the comics, Ned Leeds was a Daily Bugle reporter and (in a controversial twist) one of the men who briefly wore the Hobgoblin costume. The MCU reinvented him as Peter's best friend — a chubby, brilliant, unfailingly loyal classmate who accidentally walks in on Peter mid-suit-up.",
                "From that moment on, Ned becomes the original 'guy in the chair': remote tech support, hack-the-vending-machine specialist, and Peter's ride-or-die.",
                "His love of Star Wars LEGO sets, his crush on Betty Brant, and his absolute inability to keep a secret while being the only person who CAN keep Peter's secret made him one of the most beloved characters of the new generation of Spider-Man stories."
            ]
        },
        {
            "name": "Tony Stark",
            "role": "Mentor / Iron Man",
            "image": "/images/ally-tony-stark.png",
            "description": "Built him the Iron Spider suit, recruited him to the Avengers, and treated him like a son.",
            "first_appearance": "Tales of Suspense #39 (March 1963) — as Spider-Man's mentor: Civil War (2006)",
            "affiliations": ["Avengers", "Stark Industries", "S.H.I.E.L.D."],
            "bio": [
                "Anthony Edward Stark — billionaire, philanthropist, genius, ex-playboy — is the man who turned Spider-Man from a friendly-neighborhood vigilante into a global Avenger. Tony recruited Peter during the Superhuman Registration Civil War, designed him the nano-tech Iron Spider armor, and (regrettably) convinced him to publicly unmask.",
                "Their relationship soured during Civil War, healed in the years that followed, and was reborn in the MCU as one of Marvel's most powerful father-son arcs. Tony saw himself in Peter: brilliant, broken, desperate to be useful.",
                "His final words to Spider-Man — 'I just wanted to take care of you' — are the legacy Peter carries into every fight that follows. With great mentors come great responsibilities."
            ]
        }
    ],
    "suits": [
        {
            "name": "Classic Red & Blue",
            "era": "1962 — Today",
            "color_primary": "#E23636",
            "color_secondary": "#0059BF",
            "description": "The original. Hand-stitched by Peter himself in a Queens basement. Black web pattern, oversized eye lenses, and a logo that's outlasted four U.S. presidents.",
            "abilities": ["Mechanical Web-Shooters", "Reinforced Stitching", "Iconic Status"]
        },
        {
            "name": "Black Symbiote Suit",
            "era": "Secret Wars (1984)",
            "color_primary": "#0A0A0A",
            "color_secondary": "#FFFFFF",
            "description": "Picked up on Battleworld, this 'costume' was actually an alien lifeform. It made Peter stronger, faster, and meaner — until he ripped it off in a church belfry.",
            "abilities": ["Self-Repairing", "Unlimited Webbing", "Amplified Strength", "Aggression Boost"]
        },
        {
            "name": "Iron Spider",
            "era": "Civil War (2006)",
            "color_primary": "#B91C1C",
            "color_secondary": "#FACC15",
            "description": "Tony Stark's gift: a nano-tech suit with three articulated waldoes folded out of the back. Bulletproof, fireproof, and frankly showing off.",
            "abilities": ["Stark Nanotech", "Spider-Legs", "HUD Targeting", "Re-breather"]
        },
        {
            "name": "Stealth 'Big Time' Suit",
            "era": "2010",
            "color_primary": "#0F172A",
            "color_secondary": "#22D3EE",
            "description": "Designed by Peter at Horizon Labs. Bends light and dampens sound. Spider-Sense in cyan, ninja in matte black.",
            "abilities": ["Light-Bending", "Sound Dampening", "Customizable Tactical Modes"]
        }
    ],
    "movies": [
        {
            "title": "Spider-Man: No Way Home",
            "year": 2021,
            "actor": "Tom Holland",
            "embed_url": "https://www.youtube.com/embed/JfVOs4VSpmA",
            "description": "Three Peters. One multiverse. Every villain who ever killed a Spider-Man, all in one room."
        },
        {
            "title": "Spider-Man: Across the Spider-Verse",
            "year": 2023,
            "actor": "Shameik Moore (Miles Morales)",
            "embed_url": "https://www.youtube.com/embed/cqGjhVJWtEg",
            "description": "Miles Morales rockets across the multiverse and runs into the Spider-Society — and a canon event he refuses to accept."
        },
        {
            "title": "Spider-Man: Into the Spider-Verse",
            "year": 2018,
            "actor": "Shameik Moore (Miles Morales)",
            "embed_url": "https://www.youtube.com/embed/g4Hbz2jLxvQ",
            "description": "The Oscar-winning animated film that taught a generation: anyone can wear the mask."
        },
        {
            "title": "Spider-Man 3 — Symbiote Saga",
            "year": 2007,
            "actor": "Tobey Maguire",
            "embed_url": "https://www.youtube.com/embed/LbevdmWZX5g",
            "description": "Sam Raimi's final chapter: Tobey, a black symbiote suit, finger-guns, and the most divisive dance break in cinema."
        },
        {
            "title": "The Amazing Spider-Man 2",
            "year": 2014,
            "actor": "Andrew Garfield",
            "embed_url": "https://www.youtube.com/embed/nbp3Ra3Yp74",
            "description": "Andrew Garfield, Electro, and a heartbreak that fans still haven't recovered from."
        },
        {
            "title": "Spider-Man: Homecoming",
            "year": 2017,
            "actor": "Tom Holland",
            "embed_url": "https://www.youtube.com/embed/n9DwoQ7HWvI",
            "description": "Peter's first MCU solo: high school, the Vulture, and a handmade suit Tony Stark made fun of."
        }
    ],
    "comics": [
        {"year": "1962", "issue": "Amazing Fantasy #15", "headline": "First Appearance", "summary": "Stan Lee and Steve Ditko introduce the world to a teenage hero in a 11-page back-up story nobody expected to last."},
        {"year": "1963", "issue": "Amazing Spider-Man #1", "headline": "Solo Series Begins", "summary": "Spider-Man earns his own monthly. The Chameleon, the Fantastic Four, and a New York that hates and fears him."},
        {"year": "1973", "issue": "Amazing Spider-Man #121", "headline": "The Night Gwen Stacy Died", "summary": "The Green Goblin throws Gwen off the George Washington Bridge. The Bronze Age of comics begins on the next page."},
        {"year": "1984", "issue": "Secret Wars #8", "headline": "The Black Costume", "summary": "Peter swaps his red-and-blues for a sleek black suit — that turns out to be alive."},
        {"year": "1988", "issue": "Amazing Spider-Man #300", "headline": "Venom Arrives", "summary": "Eddie Brock and the rejected symbiote bond. A new icon is born."},
        {"year": "2011", "issue": "Ultimate Fallout #4", "headline": "Enter Miles Morales", "summary": "After Ultimate Peter Parker's death, a half-Black half-Latino kid from Brooklyn picks up the mask."},
        {"year": "2018", "issue": "Spider-Geddon", "headline": "Spider-Verse Expands", "summary": "Spider-Gwen, Spider-Man Noir, Spider-Ham, SP//dr — every Spider, every universe, all at once."}
    ]
}


# =====================
# Routes
# =====================
@api_router.get("/")
async def root():
    return {"message": "Welcome to the Spider-Man Multiverse API", "version": "1.0"}


@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_obj = StatusCheck(**input.model_dump())
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    await db.status_checks.insert_one(doc)
    return status_obj


@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    return status_checks


@api_router.get("/spiderman/all")
async def get_all_spiderman():
    """Returns the entire Spider-Man database in one call."""
    return SPIDERMAN_DB


@api_router.get("/spiderman/{section}")
async def get_section(section: str):
    """Returns a single section: origin, powers, villains, allies, suits, movies, comics."""
    if section not in SPIDERMAN_DB:
        raise HTTPException(status_code=404, detail=f"Section '{section}' not found")
    return {"section": section, "data": SPIDERMAN_DB[section]}


# =====================
# Auth Endpoints
# =====================
@api_router.post("/auth/register", response_model=AuthResponse)
async def register(payload: RegisterRequest):
    email = payload.email.lower()
    existing = await db.users.find_one({"email": email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_id = str(uuid.uuid4())
    user_doc = {
        "id": user_id,
        "email": email,
        "name": payload.name.strip(),
        "password_hash": hash_password(payload.password),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    await db.users.insert_one(user_doc)
    token = create_access_token(user_id, email)
    return AuthResponse(
        user=UserResponse(id=user_id, email=email, name=user_doc["name"]),
        token=token,
    )


@api_router.post("/auth/login", response_model=AuthResponse)
async def login(payload: LoginRequest):
    email = payload.email.lower()
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token(user["id"], email)
    return AuthResponse(
        user=UserResponse(id=user["id"], email=email, name=user["name"]),
        token=token,
    )


@api_router.get("/auth/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    return UserResponse(id=current_user["id"], email=current_user["email"], name=current_user["name"])


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
