# Dispositions-Tool 🚀

Webbasiertes Dispositionssystem zur Verwaltung, Zuteilung und Abrechnung von Handwerksaufträgen (Elektro, Klempner) in ganz Spanien.

## 📋 Überblick

Dieses System bildet den kompletten Workflow digital ab:
- Auftragserfassung
- Disposition mit Drag & Drop
- Live-Tracking der Monteure
- Statusverfolgung in Echtzeit
- Abrechnung mit Monteuren

## 🛠 Technologie-Stack

### Backend
- **Node.js** 20+ LTS
- **Express** - REST API
- **TypeScript** - Type Safety
- **PostgreSQL** 15+ mit PostGIS - Datenbank
- **Socket.io** - WebSocket für Echtzeit-Updates

### Frontend
- **React** 18+
- **TypeScript**
- **Vite** - Build Tool
- **React Router** - Navigation
- **Axios** - HTTP Client

### Mobile
- **React Native** - iOS & Android App
- GPS-Tracking für Monteure

### Infrastructure
- **Docker** & **Docker Compose**
- **GitHub Actions** - CI/CD

## 📁 Projekt-Struktur

```
.
├── backend/          # Node.js + Express Backend
│   ├── src/
│   │   ├── controllers/  # Route Controller
│   │   ├── models/       # Datenbank-Modelle
│   │   ├── routes/       # API Routes
│   │   ├── middleware/   # Express Middleware
│   │   ├── config/       # Konfiguration
│   │   └── index.ts      # Entry Point
│   ├── package.json
│   └── tsconfig.json
├── frontend/         # React Frontend
│   ├── src/
│   │   ├── components/   # React Components
│   │   ├── views/        # Pages/Views
│   │   ├── router/       # Routing
│   │   ├── store/        # State Management
│   │   └── main.ts       # Entry Point
│   ├── package.json
│   └── tsconfig.json
├── mobile/           # React Native App
│   ├── src/
│   │   ├── screens/      # App Screens
│   │   ├── components/   # React Native Components
│   │   └── App.tsx       # Entry Point
│   └── package.json
├── docker-compose.yml    # Docker Setup
└── README.md             # Diese Datei
```

## 🚀 Quick Start

### Voraussetzungen

- **Node.js** 20+ LTS ([Download](https://nodejs.org/))
- **Docker** & **Docker Compose** ([Download](https://www.docker.com/))
- **Git** ([Download](https://git-scm.com/))

### Installation

1. **Repository klonen**
```bash
git clone https://github.com/ElyasRa/NightDUTY_Abfragetool.git
cd NightDUTY_Abfragetool
```

2. **Dependencies installieren**
```bash
npm install
```

3. **Environment Variables einrichten**
```bash
cp backend/.env.example backend/.env
# Passe die Werte in backend/.env an
```

4. **Projekt starten (mit Docker)**
```bash
docker-compose up
```

Das war's! 🎉

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:3000
- **PostgreSQL**: localhost:5432

### Entwicklung ohne Docker

**Backend starten:**
```bash
cd backend
npm install
npm run dev
```

**Frontend starten:**
```bash
cd frontend
npm install
npm run dev
```

## 📝 Verfügbare Scripts

### Root-Level
```bash
npm run dev          # Startet alle Services
npm run build        # Baut alle Projekte
npm run test         # Führt alle Tests aus
```

### Backend
```bash
npm run dev          # Development Server mit Hot-Reload
npm run build        # Production Build
npm run start        # Production Server
npm run migrate      # Datenbank-Migrationen ausführen
```

### Frontend
```bash
npm run dev          # Development Server
npm run build        # Production Build
npm run preview      # Preview Production Build
```

## 🗄 Datenbank

### PostgreSQL mit PostGIS

Die Datenbank wird automatisch via Docker Compose erstellt.

**Manuelle Verbindung:**
```bash
docker-compose exec postgres psql -U dispositions -d dispositions_db
```

### Migrationen

```bash
cd backend
npm run migrate
```

## 🌐 API Dokumentation

### Health Check
```
GET /health
```

Weitere API-Endpunkte werden nach und nach hinzugefügt.

## 🔐 Umgebungsvariablen

Erstelle eine `.env` Datei im `backend/` Ordner:

```env
# Database
DATABASE_URL=postgresql://dispositions:password@localhost:5432/dispositions_db

# Server
PORT=3000
NODE_ENV=development

# JWT
JWT_SECRET=your-secret-key-here

# Google Maps
GOOGLE_MAPS_API_KEY=your-api-key-here

# Telegram
TELEGRAM_BOT_TOKEN=your-bot-token-here
```

## 📦 Deployment

### Docker Production Build

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 🧪 Testing

```bash
# Alle Tests
npm test

# Backend Tests
cd backend && npm test

# Frontend Tests
cd frontend && npm test
```

## 🤝 Mitarbeit

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## 📋 Issues & Roadmap

Siehe [GitHub Issues](https://github.com/ElyasRa/NightDUTY_Abfragetool/issues) für die aktuelle Roadmap.

**Aktueller Status:**
- ✅ Issue #1: Projekt-Setup & Repository-Struktur
- 🔄 Issue #2: Datenbank-Schema & Backend-Grundstruktur
- ⏳ Issue #3-#12: Weitere Features folgen

## 📄 Lizenz

Proprietary - Alle Rechte vorbehalten

## 👤 Autor

**ElyasRa**
- GitHub: [@ElyasRa](https://github.com/ElyasRa)

## 🙏 Danksagungen

Basierend auf dem Lastenheft Version 1.2 vom 02.11.2025

---

**Version:** 1.0.0  
**Datum:** 02.11.2025
