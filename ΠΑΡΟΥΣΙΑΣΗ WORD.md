# SPIDERMANIAC
## Παρουσίαση Project — Διαδραστική Ιστοσελίδα Spider-Man

**Τίτλος εργασίας:** SPIDERMANIAC
**Είδος:** Full-Stack Web Application με JWT Authentication
**Τεχνολογίες:** React, FastAPI, MongoDB, Tailwind CSS, JWT

---

## Πίνακας Περιεχομένων

1. Εισαγωγή
2. Σκοπός και στόχοι του project
3. Τεχνολογίες που χρησιμοποιήθηκαν και αιτιολόγηση επιλογών
4. Αρχιτεκτονική του συστήματος
5. Σχεδιαστική φιλοσοφία και εμπειρία χρήστη
6. Backend — server και βάση δεδομένων
7. Σύστημα authentication
8. Frontend — components και routing
9. Στυλιστική επεξεργασία και θέματα
10. Βασικές λειτουργίες
11. Παρουσίαση των ενοτήτων
12. Cinematic Transitions & Animations
13. Συμπεράσματα και μελλοντικές επεκτάσεις
14. Πηγές και βιβλιογραφία

---

## 1. Εισαγωγή

Το SPIDERMANIAC είναι μια ολοκληρωμένη διαδραστική ιστοσελίδα αφιερωμένη στον Spider-Man, έναν από τους πιο διαχρονικούς υπερήρωες της Marvel. Δεν είναι όμως άλλη μία απλή ενημερωτική σελίδα. Αποτέλεσε για μένα μια πρόκληση να φτιάξω κάτι που να μην παρουσιάζει απλώς πληροφορίες, αλλά να μεταφέρει την αίσθηση του χαρακτήρα — να σε βάλει για λίγα λεπτά στο σύμπαν του.

Η ιδέα ξεκίνησε από μια προσωπική σκέψη. Στην αρχική σελίδα του site υπάρχει η φράση *"A tribute to my hero who inspired me to be better"*. Αυτή δεν είναι μάρκετινγκ. Είναι ειλικρινής. Ο Spider-Man δεν είναι θεός όπως ο Thor, ούτε δισεκατομμυριούχος όπως ο Iron Man, ούτε ήρθε από άλλον πλανήτη όπως ο Superman. Είναι ένα παιδί από τα Queens που πήρε δυνάμεις και προσπάθησε, παρά τα συνεχή του λάθη, να κάνει το σωστό. Αυτή η ιδέα — ότι ο ηρωισμός δεν είναι κάτι που σου έρχεται, αλλά κάτι που διαλέγεις κάθε φορά — ήταν αυτή που με τράβηξε προς αυτόν τον χαρακτήρα από μικρός.

Η εφαρμογή έχει δύο πραγματικά διαφορετικά "σύμπαντα" τα οποία ο επισκέπτης μπορεί να επιλέξει: το **classic red** σύμπαν που τιμά τον παραδοσιακό Spider-Man με την κόκκινη και μπλε στολή και την κλασική comic-book αισθητική, και το **black symbiote** σύμπαν που εστιάζει στη σκοτεινή του πλευρά, στην ιστορία της εξωγήινης μαύρης στολής που τον επηρέασε ψυχολογικά για περισσότερο από έναν χρόνο. Κάθε σύμπαν έχει διαφορετική χρωματική παλέτα, διαφορετική τυπογραφία, διαφορετική ιστορία προέλευσης και διαφορετική αισθητική.

Η είσοδος στην εφαρμογή είναι εμπνευσμένη από κινηματογραφικά websites που βασίζονται σε scroll-driven αφήγηση. 
Ο επισκέπτης ξεκινάει με ένα μαύρο φόντο και την προαναφερθείσα ατάκα, κάνει scroll για να δει το μανιφέστο των δύο πλευρών του ήρωα, και στη συνέχεια επιλέγει σε ποιο σύμπαν θέλει να μπει.

---

## 2. Σκοπός και στόχοι του project

### Πρωτεύοντες στόχοι

Από τεχνική σκοπιά, στόχος ήταν να φτιάξω μια εφαρμογή που να καλύπτει ολόκληρο τον κύκλο ανάπτυξης ενός σύγχρονου web application:

- Σχεδίαση και υλοποίηση ενός RESTful API με σύγχρονο async framework.
- Δημιουργία μιας component-based διεπαφής στο frontend, με σαφή διαχωρισμό αρμοδιοτήτων ανάμεσα στα κομμάτια.
- Ενσωμάτωση **πλήρους συστήματος authentication** με JWT tokens, εγγραφή χρηστών, σύνδεση και προστατευμένα endpoints.
- **Πολλαπλά routes** με React Router, ώστε διαφορετικές διαδρομές του site να εμφανίζουν εντελώς διαφορετικά layouts.
- Δημιουργία διαδραστικού canvas-based **particle field** που αντιδρά στην κίνηση του ποντικιού, προσομοιώνοντας ιστούς αράχνης ή συμβιωτικά πλοκάμια.
- Cinematic scroll-driven landing page με parallax effects.

### Δευτερεύοντες στόχοι

Πέρα από τους τεχνικούς στόχους, υπήρξαν και αρκετοί σχεδιαστικοί:

- Δημιουργία μιας οπτικής γλώσσας που να ξεχωρίζει από τη συνηθισμένη "AI-generated" αισθητική (όχι μωβ gradients, όχι Inter font, όχι ίδιες κάρτες με όλους).
- Δύο πραγματικά διακριτές αισθητικές για τα δύο σύμπαντα, όχι απλώς εναλλαγή χρωμάτων.
- Ενσωμάτωση comic-book τυπογραφίας (Bangers) που να μεταφέρει αμέσως τον επισκέπτη στον κόσμο των κόμικς.

---

## 3. Τεχνολογίες που χρησιμοποιήθηκαν και αιτιολόγηση επιλογών

Κάθε τεχνολογία επιλέχθηκε για συγκεκριμένους λόγους που σχετίζονται με τις απαιτήσεις του project, την παραγωγικότητα κατά την ανάπτυξη και τη μακροπρόθεσμη συντηρησιμότητα του κώδικα.

### 3.1 Γιατί επιλέχθηκε η Python για το backend

Η Python θεωρείται μία από τις πιο αναγνώσιμες γλώσσες προγραμματισμού, με σύνταξη που μοιάζει σχεδόν με ψευδοκώδικα. Διαθέτει επίσης τεράστιο οικοσύστημα βιβλιοθηκών για ανάπτυξη web εφαρμογών και επεξεργασία δεδομένων. Σε σύγκριση με γλώσσες όπως η Java, η Python απαιτεί λιγότερες γραμμές κώδικα για την ίδια λειτουργικότητα. Σε σχέση με τη JavaScript στο backend (Node.js), προσφέρει καθαρότερη σύνταξη.

### 3.2 Γιατί επιλέχθηκε το FastAPI

Το FastAPI ξεχωρίζει για τρεις βασικούς λόγους. Πρώτον, είναι ένα από τα ταχύτερα Python web frameworks επειδή βασίζεται σε Starlette και Uvicorn, που υποστηρίζουν asynchronous κλήσεις. Δεύτερον, παράγει αυτόματα τεκμηρίωση Swagger UI για το API. Τρίτον, ενσωματώνει το Pydantic για validation των δεδομένων εισόδου.

Εναλλακτικές επιλογές ήταν το Flask (πολύ ελαφρύ, αλλά απαιτεί χειροκίνητη υλοποίηση πολλών λειτουργιών) και το Django (πολύ πλήρες, αλλά υπερβολικά βαρύ για ένα μικρό project).

### 3.3 Γιατί επιλέχθηκε η MongoDB

Η MongoDB είναι NoSQL βάση που αποθηκεύει δεδομένα σε μορφή BSON, παρόμοια με JSON. Για το συγκεκριμένο project όπου τα δεδομένα έχουν εμφωλιασμένη δομή (κάθε χαρακτήρας περιέχει λίστες από βιογραφικές παραγράφους, συνεργασίες κ.λπ.), η MongoDB είναι φυσική επιλογή. Σε σχεσιακή βάση θα απαιτούσε πολλούς πίνακες και πολύπλοκα joins.

### 3.4 Γιατί JWT αντί για session-based authentication

Επέλεξα JWT (JSON Web Tokens) γιατί είναι stateless — ο server δεν χρειάζεται να κρατά πίνακα ενεργών συνεδριών. Ο πελάτης κρατάει το token στο localStorage και το στέλνει σε κάθε αίτηση μέσω του Authorization header. Σε σύγκριση με τα session cookies, τα JWT τοkens είναι πιο εύκολα να επεκταθούν σε microservices ή native apps στο μέλλον. Για ένα project μικρής κλίμακας με μία υπηρεσία, και τα δύο θα δούλευαν, αλλά τα JWT είναι το σύγχρονο πρότυπο για REST APIs.

### 3.5 Γιατί επιλέχθηκε η React

Η React είναι η πιο δημοφιλής βιβλιοθήκη JavaScript για interactive UIs. Επιλέχθηκε για τέσσερις βασικούς λόγους: τη component-based αρχιτεκτονική, το virtual DOM (μόνο τα στοιχεία που άλλαξαν επανασχεδιάζονται), την τεράστια κοινότητα και το οικοσύστημα συμπληρωματικών βιβλιοθηκών (React Router, Axios, Shadcn UI).

### 3.6 Γιατί επιλέχθηκε το React Router

Με το upgrade σε δύο πραγματικά διαφορετικά σύμπαντα (`/classic` και `/symbiote`), χρειαζόμουν proper client-side routing. Το React Router είναι το de facto πρότυπο για navigation σε React εφαρμογές και υποστηρίζει μεταξύ άλλων nested routes, URL parameters και προγραμματιστική πλοήγηση.

### 3.7 Γιατί επιλέχθηκε η Tailwind CSS

Η Tailwind είναι utility-first CSS βιβλιοθήκη. Αντί να γράφω custom CSS classes σε εξωτερικά αρχεία, χρησιμοποιώ έτοιμες utility classes απευθείας στα HTML elements. Αυτό έχει τρία πλεονεκτήματα: μειώνει δραστικά τον χρόνο ανάπτυξης, εξασφαλίζει συνέπεια στο design (όλα τα styling values προέρχονται από ένα κεντρικό config), και παράγει μικρά bundles επειδή κατά το build process αφαιρούνται οι αχρησιμοποίητες classes.

Σε σύγκριση με το Bootstrap, η Tailwind δεν επιβάλλει συγκεκριμένη οπτική ταυτότητα, κάτι κρίσιμο για το SPIDERMANIAC που ήθελε να έχει απολύτως δική του αισθητική.

### 3.8 Γιατί επιλέχθηκε το Shadcn UI

Το Shadcn UI δεν είναι κλασική βιβλιοθήκη components. Παρέχει components που αντιγράφονται απευθείας στον κώδικα — έχω πλήρη έλεγχο, μπορώ να τα τροποποιήσω, και δεν εξαρτώμαι από εξωτερικές ενημερώσεις. Βασίζεται στο Radix UI, το οποίο διαχειρίζεται όλα τα δύσκολα ζητήματα προσβασιμότητας (πλοήγηση πληκτρολογίου, screen readers, focus management σε modals).

### 3.9 Γιατί χρησιμοποιήθηκαν οι γραμματοσειρές Bangers και Outfit

Η επιλογή των γραμματοσειρών ήταν κομβικό σχεδιαστικό στοιχείο. Η **Bangers** είναι display font που μιμείται τη χειρόγραφη γραφή των αμερικανικών κόμικς του 1960 — μεταφέρει τον επισκέπτη στον κόσμο των κόμικς ακόμα πριν διαβάσει το κείμενο. Η **Outfit** είναι μοντέρνα sans-serif γραμματοσειρά με εξαιρετική αναγνωσιμότητα, για το κυρίως κείμενο. Αποφεύχθηκαν συνειδητά οι υπερβολικά χρησιμοποιημένες Inter, Roboto και Arial.

### 3.10 Γιατί χρησιμοποιήθηκε HTML Canvas για τα particles

Για τα particles που ακολουθούν το ποντίκι και σχηματίζουν συμβιωτικά πλοκάμια, χρησιμοποίησα το HTML5 Canvas API. Το ίδιο αποτέλεσμα θα μπορούσε να επιτευχθεί με SVG ή ακόμα και CSS animations, αλλά το Canvas προσφέρει πολύ καλύτερη απόδοση όταν σχεδιάζονται δεκάδες κινούμενα στοιχεία ταυτόχρονα. Επιπλέον, επιτρέπει pixel-level έλεγχο για εφέ όπως radial gradients και symbiote highlights.

---

## 4. Αρχιτεκτονική του συστήματος

Το project ακολουθεί κλασική αρχιτεκτονική τριών επιπέδων:

```
┌──────────────────────────────────────────┐
│         FRONTEND (Port 3000)             │
│  React + Router + Tailwind + Shadcn      │
│  + Canvas Particles + Auth Context       │
└────────────────┬─────────────────────────┘
                 │ HTTP / REST API
                 │ /api/*
                 ▼
┌──────────────────────────────────────────┐
│         BACKEND (Port 8001)              │
│       FastAPI + Pydantic + JWT           │
└────────────────┬─────────────────────────┘
                 │ Motor (async driver)
                 ▼
┌──────────────────────────────────────────┐
│            MongoDB Database               │
│         users + status_checks             │
└──────────────────────────────────────────┘
```

Ο χρήστης αλληλεπιδρά μόνο με το frontend. Όταν ζητάει εγγραφή ή σύνδεση, το frontend στέλνει POST στα `/api/auth/register` ή `/api/auth/login`. Ο server επιστρέφει JWT token, το οποίο αποθηκεύεται στο localStorage και αποστέλλεται μέσω Authorization header σε όλες τις επόμενες αιτήσεις. Τα δεδομένα του Spider-Man, για λόγους απόδοσης και επειδή το site λειτουργεί και ως static experience, είναι ενσωματωμένα στο frontend ως JavaScript module.

---

## 5. Σχεδιαστική φιλοσοφία και εμπειρία χρήστη

Ο σχεδιασμός βασίστηκε σε δύο αρχές: **κινηματογραφικότητα** και **κωμικό αρχέτυπο**. Ο επισκέπτης δεν "διαβάζει" το site· "μπαίνει" σε αυτό.

### Cinematic intro

Στην πρώτη επίσκεψη παίζει σύντομη ταινία intro: μαύρη οθόνη, λευκές συμβιωτικές σταγόνες πέφτουν από πάνω, εμφανίζεται το spider logo, μετά το λογότυπο SPIDERMANIAC, μετά η ατάκα. Skip με click. Δεν επαναλαμβάνεται στην ίδια συνεδρία (sessionStorage flag).

### GTA 6-style scroll prologue

Μετά το intro, ο επισκέπτης βλέπει σελίδα που αποτελείται από τρεις διαδοχικές οθόνες scroll. Πρώτα έρχεται το quote *"A tribute to my hero who inspired me to be better"* με τον Black Spider-Man σαν φόντο, με parallax effect. Έπειτα το μανιφέστο "Two Sides. One Hero." με φωτογραφίες των δύο εκδοχών αριστερά-δεξιά. Τέλος, το split-screen choice που οδηγεί στο `/classic` ή `/symbiote`.

### Δύο διακριτά σύμπαντα

Το `/classic` είναι κωμικό: λευκό φόντο, παχιά μαύρα borders, halftone dots, σκιές offset, κόκκινες και μπλε αποχρώσεις. Το `/symbiote` είναι κινηματογραφικό: μαύρο φόντο, λεπτά γκρι borders, λάμψεις, glass-morphism, συμβιωτικές σταγόνες σε γωνίες των ενοτήτων. Η ίδια η ιστορία προέλευσης που εμφανίζεται είναι διαφορετική: στο classic διαβάζεις την κανονική origin του Peter (το δάγκωμα της αράχνης, ο θάνατος του Uncle Ben), στο symbiote διαβάζεις την ιστορία του Black Suit (Battleworld, ο εκκλησιαστικός πύργος, η γέννηση του Venom).

---

## 6. Backend — server και βάση δεδομένων

Το backend βρίσκεται σε ένα αρχείο, το `backend/server.py`. Περιλαμβάνει τη σύνδεση με τη MongoDB, τα auth helpers (bcrypt + JWT), τα Pydantic models, τη βάση δεδομένων του Spider-Man ως Python dictionary, και τα API endpoints.

### Αρχικοποίηση

```python
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
import os, bcrypt, jwt
from datetime import datetime, timezone, timedelta

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

JWT_SECRET = os.environ['JWT_SECRET']
JWT_ALGORITHM = "HS256"
TOKEN_EXPIRY_HOURS = 24

app = FastAPI(title="Spider-Man Multiverse API")
api_router = APIRouter(prefix="/api")
```

### Παράδειγμα endpoint για τα δεδομένα Spider-Man

```python
@api_router.get("/spiderman/{section}")
async def get_section(section: str):
    if section not in SPIDERMAN_DB:
        raise HTTPException(status_code=404, detail=f"Section '{section}' not found")
    return {"section": section, "data": SPIDERMAN_DB[section]}
```

### Στατιστικά της βάσης

- 6 villains με πλήρη βιογραφικά (Green Goblin, Venom, Doctor Octopus, Sandman, Lizard, Mysterio)
- 6 σύμμαχοι με βιογραφικά (MJ, Aunt May, Miles Morales, Gwen Stacy, Ned Leeds, Tony Stark)
- 6 υπερδυνάμεις του Spider-Man
- 4 εμβληματικές στολές
- 6 YouTube trailers (μεταξύ άλλων το πρόσφατο Spider-Man: Brand New Day του 2026)
- 7 σταθμοί στην ιστορία των κόμικς (1962-2018)
- 2 διαφορετικές εκδοχές της ιστορίας προέλευσης (κλασική και symbiote)

---

## 7. Σύστημα authentication

Το σύστημα authentication βασίζεται σε JWT tokens. Οι κωδικοί κατακερματίζονται με bcrypt πριν αποθηκευτούν στη MongoDB.

### Hashing και επαλήθευση κωδικού

```python
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
```

### Δημιουργία JWT token

```python
def create_access_token(user_id: str, email: str) -> str:
    payload = {
        "sub": user_id,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=24),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")
```

### Endpoint εγγραφής

```python
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
```

### Στο frontend — AuthContext

Στο React χρησιμοποιείται ένα Context Provider που αποθηκεύει τον τρέχοντα χρήστη και το token. Όταν ο χρήστης κάνει refresh τη σελίδα, το AuthContext καλεί το `/api/auth/me` με το αποθηκευμένο token για να ελέγξει αν είναι ακόμα έγκυρο.

```jsx
useEffect(() => {
    const token = localStorage.getItem("spidermaniac_token");
    if (!token) { setLoading(false); return; }
    axios.get(`${API}/auth/me`, {
        headers: { Authorization: `Bearer ${token}` }
    })
    .then((res) => setUser(res.data))
    .catch(() => localStorage.removeItem("spidermaniac_token"))
    .finally(() => setLoading(false));
}, []);
```

---

## 8. Frontend — components και routing

### Δομή των routes

```jsx
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Landing />} />
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />
    <Route path="/classic" element={<Universe />} />
    <Route path="/symbiote" element={<Universe />} />
    <Route path="*" element={<Navigate to="/" replace />} />
  </Routes>
</BrowserRouter>
```

Η ίδια Universe component εξυπηρετεί και τα δύο σύμπαντα. Διαβάζει το pathname από το React Router και προσαρμόζει τα θέματα και την ιστορία προέλευσης ανάλογα.

### Ιεραρχία components

```
App.js
├── Toaster (sonner)
├── CinematicIntro
└── BrowserRouter
    ├── Landing (3-section parallax scroll)
    │   ├── Quote section
    │   ├── Manifesto section
    │   └── Choice section (split-screen)
    ├── Login
    ├── Register
    └── Universe (one component, two routes)
        ├── ParticleField (mouse-following tendrils)
        ├── Navbar (with auth dropdown)
        ├── Hero
        ├── Origin (different per universe)
        ├── Powers
        ├── Villains (with character modal)
        ├── Suits
        ├── Allies (with character modal)
        ├── Trailers
        ├── Comics
        └── Footer
```

---

## 9. Στυλιστική επεξεργασία και θέματα

Το αρχείο `frontend/src/index.css` συγκεντρώνει όλους τους CSS κανόνες των δύο θεμάτων. Όλα τα styling αποφάσεις (χρώματα, borders, σκιές, animations) εφαρμόζονται μέσω class composition.

### Classic Red Theme

```css
.theme-red {
    background-color: #F5F5F5;
    background-image: radial-gradient(
        rgba(0,0,0,0.08) 1.2px,
        transparent 1.2px
    );
    background-size: 24px 24px;
}

.theme-red .surface {
    background: #FFFFFF;
    border: 4px solid #000;
    box-shadow: 8px 8px 0 0 #000;
    border-radius: 0;
}
```

### Symbiote Black Theme

```css
.theme-black {
    background-color: #050505;
    color: #F5F5F5;
}

.theme-black .surface {
    background: #111111;
    border: 1px solid #2a2a2a;
    border-radius: 16px;
    backdrop-filter: blur(6px);
}
```

### Universe entry animation

Κάθε φορά που ο χρήστης φτάνει σε `/classic` ή `/symbiote`, παίζει μια animation που κάνει την οθόνη να γλιστράει προς τα πάνω με ελαφρύ blur:

```css
@keyframes universe-fade-in {
    0%   { opacity: 0; transform: translateY(40px) scale(0.98); filter: blur(8px); }
    100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
}
```

---

## 10. Βασικές λειτουργίες

### 10.1 Cinematic intro

Στην πρώτη επίσκεψη της συνεδρίας παίζει 4-δευτερόλεπτο intro: μαύρη οθόνη, λευκές συμβιωτικές σταγόνες πέφτουν από πάνω σαν βροχή, εμφανίζεται το spider logo με zoom-in, μετά το λογότυπο SPIDERMANIAC, μετά η ατάκα *"A tribute to the hero who inspired me to be better"*. Skip με click. Αποθηκεύεται στο sessionStorage ώστε να μην επαναλαμβάνεται.

### 10.2 Style scroll prologue

Η αρχική σελίδα (`/`) είναι χωρισμένη σε τρεις vertical sections. Καθώς ο χρήστης κάνει scroll, το background κινείται με parallax (λιγότερο γρήγορα από τον foreground), το κείμενο fade-άρει σταδιακά, και οι εικόνες αναπνέουν με ελαφριές κινήσεις. Είναι εμπνευσμένο από κινηματογραφικά websites.

### 10.3 Σύστημα authentication

Ο χρήστης μπορεί να εγγραφεί ή να συνδεθεί από οπουδήποτε στο site (Navbar dropdown, Landing top-right). Μετά την επιτυχή σύνδεση, εμφανίζεται "Hi, [όνομα]" στη navigation. Το logout διαγράφει το token και επιστρέφει στην αρχική σελίδα.

### 10.4 Mouse-following symbiote tendrils

Σε όλο το site (όχι μόνο στο symbiote universe), όπου κουνάει το ποντίκι ο χρήστης, εμφανίζονται **πέντε καμπυλωτά πλοκάμια** που κυματίζουν και τον ακολουθούν. Το χρώμα ποικίλλει ανά θέμα: στο classic είναι κόκκινα, στο symbiote είναι μαύρα με λευκό περίγραμμα. Το εφέ είναι υλοποιημένο με HTML Canvas και Bezier curves.

### 10.5 Δύο πραγματικά διαφορετικά σύμπαντα

Το `/classic` και το `/symbiote` δεν είναι απλά μια εναλλαγή χρωμάτων· εμφανίζουν διαφορετική ιστορία προέλευσης (κανονική vs symbiote saga), διαφορετικές παλέτες, διαφορετικές τυπογραφικές αποφάσεις, διαφορετικές animations, και διαφορετικές αισθήσεις. Είναι σαν να επισκέπτεσαι δύο διαφορετικά websites αφιερωμένα στον ίδιο ήρωα.

### 10.6 Διαδραστικά bio modals

Κάθε κάρτα villain ή ally είναι clickable. Με κλικ ανοίγει modal με μεγάλη εικόνα, πλήρες όνομα, πρώτη εμφάνιση στα κόμικς, ομάδες, υπερδύναμη ή ρόλος, και τριμερές αναλυτικό βιογραφικό.

### 10.7 YouTube trailers με playlist

Έξι trailers ταινιών, μεταξύ των οποίων το ολοκαίνουργιο Spider-Man: Brand New Day του 2026. Featured player + playlist· κλικ σε διαφορετικό item αλλάζει το iframe.

---

## 11. Παρουσίαση των ενοτήτων

### 11.1 Hero
Δυναμική κεντρική παρουσίαση. Στο classic γράφει "THWIP! YOUR FRIENDLY NEIGHBORHOOD SPIDER-MAN", στο symbiote γράφει "BLACK SYMBIOTE AWAKENS". Διαφορετική εικόνα ανά σύμπαν.

### 11.2 Origin
Δύο εκδοχές. Στο classic διαβάζεις πώς ο Peter δαγκώθηκε από την αράχνη και πώς ο θάνατος του Uncle Ben τον έκανε ήρωα. Στο symbiote διαβάζεις πώς πήρε τη μαύρη στολή από το Battleworld, πώς τον επηρέασε ψυχολογικά, και πώς στον εκκλησιαστικό πύργο γέννησε τον Venom.

### 11.3 Powers
Έξι κάρτες με τις υπερδυνάμεις: Wall-Crawling, Spider-Sense, Superhuman Strength, Web-Shooters, Reflexes & Agility, Genius Intellect.

### 11.4 Rogues Gallery
Έξι villains ταξινομημένοι κατά απειλή (Omega, Alpha, Beta).

### 11.5 Iconic Suits
Τέσσερις στολές: Classic Red & Blue, Black Symbiote, Iron Spider, Stealth "Big Time".

### 11.6 The Web of Family
Έξι σύμμαχοι του Spider-Man.

### 11.7 Official Trailers
Έξι ταινίες, με featured player και playlist navigation. Περιλαμβάνει και το νέο Spider-Man: Brand New Day του 2026.

### 11.8 Comics Timeline
Επτά κρίσιμα γεγονότα από την ιστορία των κόμικς, από το Amazing Fantasy #15 του 1962 μέχρι το Spider-Geddon του 2018.

---

## 11.9 Cinematic Transitions & Animations (νέα προσθήκη)

Στην τελική έκδοση του SPIDERMANIAC ενσωματώθηκε ένα ολοκληρωμένο σύστημα GTA-6 style cinematic transitions, χρησιμοποιώντας τη βιβλιοθήκη **framer-motion** σε συνεργασία με τον React Router. Στόχος ήταν να μη φαίνεται ποτέ "απλή αλλαγή σελίδας", αλλά κάθε route να ζει σαν σκηνή ταινίας.

### Σύστημα Page Transitions

Δημιουργήθηκε το component `PageTransition.jsx` που τυλίγει κάθε route και εφαρμόζει διαφορετικό variant animation ανάλογα με το destination:

- **Landing (`/`)**: Αργό cinematic scale-in με blur και brightness ramp (1.1s). Δίνει την αίσθηση ότι η κάμερα ζουμάρει σε ένα νέο σύμπαν.
- **Auth (`/login`, `/register`)**: Slide-up από κάτω με ελαφρύ blur (0.9s). Πιο τεχνικό, σαν να εμφανίζεται διεπαφή terminal.
- **Classic (`/classic`)**: Bold side-slide από δεξιά με zoom-out. Συνοδεύεται από κόκκινο-μπλε χρωματικό sweep overlay (signature χρώματα του Spider-Man).
- **Symbiote (`/symbiote`)**: Glitchy hue-rotate + warp + λευκό symbiote sweep — έντονη, διαστροφική αίσθηση που ταιριάζει με το alien lifeform.

Επιπλέον, σε κάθε route mount τρέχουν τρία ταυτόχρονα layers: το **WipeCurtain** που σαρώνει το screen διαγωνίως, το **FlashPulse** που δίνει ένα γρήγορο φως-αναβόσβημα, και το variant transition του ίδιου του route.

### Venom Takeover — η "jumpscare" είσοδος στο Symbiote

Η μετάβαση στο Black Symbiote universe δεν είναι απλώς animation. Είναι μια ολοκληρωμένη σκηνή 1.6 δευτερολέπτων:

1. **Tendrils**: Οκτώ μαύρες symbiote-φυσαλίδες ξεσπούν από κάθε γωνία και κάθε άκρη της οθόνης, διαστέλλονται 4× και καλύπτουν τα πάντα.
2. **SVG Tentacle Strands**: Οκτώ jagged μαύρες δεσμίδες σχεδιάζονται με `pathLength` animation από τα όρια προς το κέντρο, σαν συνέχεια του symbiote.
3. **Spider Symbol Burst**: Στο κέντρο της οθόνης εκρήγνυται ένα τεράστιο λευκό spider symbol με glow, που scale-bounce-shrinks (0 → 1.6 → 1.2 → 0).
4. **White Flash**: Σύντομο λευκό φλας στο peak (0.5 opacity για 0.15s) που δίνει την punchline αίσθηση.

Το αποτέλεσμα είναι ότι όταν ο χρήστης πατάει "UNLEASH →" στο landing, νιώθει ότι το symbiote τον αρπάζει — όπως ο Eddie Brock στο Venom (2018) ή ο Peter στο Spider-Man 3 (2007).

### Scroll-Triggered Reveals

Όλα τα sections μέσα στο Universe page (Origin, Powers, Villains, Suits, Allies, Trailers, Comics) τυλίγονται σε ένα `ScrollReveal` component που χρησιμοποιεί το `whileInView` του framer-motion. Καθώς ο χρήστης σκρολάρει, κάθε section:

- Ξεκινάει με `opacity: 0`, `y: 80`, `blur(8px)`, `scale: 0.97`
- Καθώς το 15% του ύψους του γίνεται ορατό στο viewport, τρέχει cubic-bezier transition (0.16, 1, 0.3, 1) με διάρκεια 0.95s
- Καταλήγει σε καθαρή, ζωντανή εμφάνιση

Έτσι η σελίδα δεν εμφανίζεται "ξαφνικά", αλλά γεμίζει σταδιακά καθώς ο χρήστης την εξερευνά — όπως στις cinematic intro σκηνές του GTA 6 reveal trailer.

### Hover Zoom στην επιλογή Universe

Στο choice section της landing, και οι δύο πλευρές (Classic / Symbiote) τώρα ζουμάρουν την εικόνα 1.18× με ελαφρύ rotation όταν περνάς από πάνω, ενώ η αντίθετη πλευρά σκουραίνει στο 30%. Παράλληλα η hovered πλευρά αποκτά colored glow (κόκκινο για Classic, λευκό για Symbiote), και το CTA button μεγαλώνει στο 110%.

### Spider Intro Logo

Στην πρώτη φόρτωση του site, το γνωστό απλό spider SVG αντικαταστάθηκε με ένα cinematic, movie-style symbiote spider:

- 8 jagged articulated legs που σχεδιάζονται με `pathLength` animation
- Pulsing aura ring (radial expansion με opacity flicker)
- Spider-web grid στο background
- Symbiote drip animation από την κορυφή
- Letter-spacing reveal του τίτλου SPIDERMANIAC

Η σκηνή έχει τέσσερις φάσεις (spider draws in → title → tagline → fade) και είναι skippable με click.

### Τεχνικά οφέλη

Όλες οι transitions υλοποιήθηκαν χωρίς JavaScript animation loops — χρησιμοποιείται το hardware-accelerated CSS transform/opacity μέσω του framer-motion. Αυτό σημαίνει 60fps και στις φθηνότερες συσκευές, και καμία επίπτωση στο SEO επειδή το περιεχόμενο πάντα υπάρχει στο DOM, απλώς αλλάζει το optical state του.

---

## 12. Συμπεράσματα και μελλοντικές επεκτάσεις

### Τι αποκόμισα από αυτό το project

Η ολοκλήρωση του SPIDERMANIAC ήταν πολύτιμη εμπειρία. Έμαθα να σχεδιάζω μια εφαρμογή ολιστικά, να ισορροπώ ανάμεσα στις απαιτήσεις της αισθητικής και της λειτουργικότητας, και να παίρνω αποφάσεις που να εξυπηρετούν και τις δύο πλευρές. Η εμπειρία της ενσωμάτωσης συστήματος authentication με JWT, της χρήσης React Router για πραγματικά διαφορετικά routes, και της υλοποίησης Canvas-based animations με Bezier curves, με δίδαξε πολλά πέρα από τα βασικά.

Έμαθα επίσης να μην ξεκινάω τον κώδικα πριν σχεδιάσω. Πέρασα μέρες σχεδιάζοντας το flow πριν γράψω την πρώτη γραμμή — και γλίτωσα εβδομάδες ξαναγραφής.

### Μελλοντικές επεκτάσεις

- Σύστημα favorites: ο logged-in χρήστης να σώζει το αγαπημένο του σύμπαν, για να επιστρέφει αυτόματα εκεί.
- Διαδραστική ψηφοφορία: ποιος είναι ο αγαπημένος Spider-Man (Tobey, Andrew, Tom, Miles), με αποτελέσματα στη MongoDB.
- "Build Your Own Suit": ο χρήστης συνδυάζει χρώματα και υπερδυνάμεις.
- Πολυγλωσσική υποστήριξη (i18n) — ελληνικά και άλλες γλώσσες.
- Επέκταση χαρακτήρων: Vulture, Electro, Kraven, Spider-Gwen.

---

## 13. Πηγές και βιβλιογραφία

### Πηγές περιεχομένου

- Marvel Official Website — https://www.marvel.com/characters/spider-man-peter-parker
- Marvel Database (Fandom) — https://marvel.fandom.com
- YouTube Official Trailers (Sony Pictures, Marvel Studios)

### Τεχνική τεκμηρίωση

- FastAPI — https://fastapi.tiangolo.com
- React — https://react.dev
- React Router — https://reactrouter.com
- Tailwind CSS — https://tailwindcss.com/docs
- Shadcn UI — https://ui.shadcn.com
- Lucide Icons — https://lucide.dev
- MongoDB — https://www.mongodb.com/docs
- JWT (RFC 7519) — https://datatracker.ietf.org/doc/html/rfc7519

### Κόμικς που αναφέρθηκαν

- Stan Lee & Steve Ditko, *Amazing Fantasy* #15 (Marvel Comics, August 1962)
- David Michelinie & Todd McFarlane, *The Amazing Spider-Man* #300 (Marvel Comics, May 1988)
- *The Amazing Spider-Man* #316 (Marvel Comics, 1989) — quote αναφέρεται στο symbiote origin
- *Secret Wars* #8 (Marvel Comics, 1984) — όπου ο Peter αποκτά πρώτη φορά τη μαύρη στολή

---

## Δήλωση

Το παρόν project αποτελεί fan-made εκπαιδευτικό αφιέρωμα. Οι χαρακτήρες Spider-Man, Venom, Green Goblin και όλοι οι υπόλοιποι, καθώς και οι εικόνες που τους αναπαριστούν, αποτελούν πνευματική ιδιοκτησία της Marvel Comics και της Sony Pictures Entertainment. Δημιουργήθηκε αποκλειστικά για εκπαιδευτικούς σκοπούς και δεν προορίζεται για εμπορική χρήση.

---

*"A tribute to my hero who inspired me to be better."*

---

**Τέλος Παρουσίασης**
