# The Shankar Communications (TSC) QR Reward System

## 🏪 Unified QR Code Reward System for The Shankar Communications

A mobile-first, interactive web application for customer rewards and offers at The Shankar Communications (TSC) stores, accessed via QR code scanning. All branding uses:

```
The Shankar Communications
(TSC)
[Section/Context]
```

---

## 🌟 Features

- 🎡 **Spin & Win**: Complete social tasks to unlock a spin for prizes
- 🛡️ **₹19 Tempered Glass Offer**: Token-based, WhatsApp-integrated offer
- 🏪 **Multi-Store Support**: Maynaguri (MNG), Dhupguri (DPG), Jamaldaha (JMD)
- 📱 **Mobile-First**: Responsive, glassmorphism UI, golden branding
- 🔒 **Token System**: Secure, store-specific, and admin token tools
- 📊 **Progress Tracking**: localStorage for user state

---

## 📁 Project Structure

```
TSC-QR-Reward-System/
├── index.html                  # Loyalty landing page (store-specific)
├── welcome.html                # Unified reward center (choose Spin & Win or Tempered Glass)
├── tasks-new.html              # Task completion page (social media tasks)
├── reward.html                 # Spin wheel rewards page
├── tempered-glass.html         # Tempered glass offer page (token entry)
├── generate-token.html         # WhatsApp token generation (generic)
├── generate-token-mng.html     # WhatsApp token (Maynaguri)
├── generate-token-dpg.html     # WhatsApp token (Dhupguri)
├── generate-token-jmd.html     # WhatsApp token (Jamaldaha)
├── thank-you.html              # Success/completion page
├── decode-token.html           # Token decoder (internal/external)
├── token-generator-advanced.html # Advanced token generator (admin)
├── tsc-logo.jpg                # TSC branding logo
└── README.md                   # Project documentation
```

---

## 🚦 Main Flows

### 🎡 Spin & Win Flow
1. **Entry** → `welcome.html?store=MNG`
2. **Choose Spin & Win**
3. **Tasks** → `tasks-new.html` (Complete 6 social tasks: WhatsApp Join, WhatsApp Channel, Google Review, Facebook, Instagram, YouTube)
4. **Reward** → `reward.html` (Spin the wheel)
5. **Success** → `thank-you.html` (Show prize details)

### 🛡️ Tempered Glass Flow
1. **Entry** → `welcome.html?store=MNG`
2. **Choose Tempered Glass**
3. **Offer** → `tempered-glass.html` (Token entry or generation)
4. **Generate** → `generate-token.html` or store-specific token page
5. **Success** → `thank-you.html` (Token verified)

---

## 🔧 Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (all inline, no frameworks)
- **Styling**: Glassmorphism, golden color, mobile-first responsive
- **Storage**: localStorage for progress and state
- **Hosting**: GitHub Pages
- **Integration**: WhatsApp Web API for token generation

---

## 🎨 Design & Branding

- **Constant Golden Branding**: All "The Shankar Communications (TSC)" text uses a fixed golden color (`#FFD700`)
- **Glassmorphism**: Modern frosted glass UI
- **Mobile-First**: Optimized for smartphones
- **Animations**: Subtle, non-distracting
- **Accessibility**: High contrast, readable fonts

---

## 🛠️ Customization

- **Store Names**: Update in each HTML file's JS config
- **Prizes**: Edit the `prizes` array in `reward.html`
- **Social Links**: Edit task URLs in `tasks-new.html`

---

## 📊 Analytics & Tracking

- **localStorage** keys:
  - `current_store`, `completedTasks`, `hasSpun`, `wonPrize`, `verifiedToken`, `tokenType`, etc.
- **User Progress**: Tasks, spins, and tokens are tracked per session

---

## 🚀 Deployment

1. **Clone**: `git clone https://github.com/PsProsen-Dev/TSC-QR-Reward-System.git`
2. **Serve Locally**: `python -m http.server 8000` or use VS Code Live Server
3. **Deploy**: GitHub Pages (Settings → Pages → Deploy from branch)
4. **QR Codes**: Generate for each store URL:
   - `/?store=MNG`, `/?store=DPG`, `/?store=JMD`

---

## 🔒 Private Client Project

This is a proprietary project developed for **The Shankar Communications (TSC)**. 
- **Client**: The Shankar Communications
- **Developer**: PsProsen-Dev
- **Status**: Private/Commercial Project
- **Access**: Restricted to authorized personnel only

---

## 👨‍💻 Development Team & Credits

- **Lead Developer**: Prosenjit Paul (Ps Prosen)
- **Client**: The Shankar Communications (TSC)
- **Project Type**: Private Commercial Development
- **Framework**: RTX Protocol v1.5
- **Engine**: Claude Sonnet 4 + VS Code Integration
- **Design**: Gold Royal Luxe, glassmorphism, mobile-first
- **Status**: Proprietary Solution for TSC

---

## 📞 Client Support & Contact

- 📧 **Technical Support**: Contact through designated channels only
- 📱 **Client Contact**: The Shankar Communications (TSC)
- 🔧 **Developer Contact**: Ps Prosen (for authorized modifications only)
- 🚫 **Public Access**: Not available - Private commercial project

---

**Developed exclusively for The Shankar Communications (TSC)**

*Custom QR reward system solution - Proprietary & Confidential* 🔒�
