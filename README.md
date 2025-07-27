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

### 🎡 Complete Customer Journey
1. **QR Scan** → `index.html?store=MNG` (Store-specific landing page)
2. **Get Started** → Click button to go to `welcome.html?store=MNG` 
3. **Choose Reward** → Select "Spin & Win" or "Tempered Glass"
4. **Complete Tasks** → `tasks-new.html` (6 social tasks) OR Token entry
5. **Claim Reward** → `reward.html` (Spin wheel) OR `tempered-glass.html`
6. **Success** → `thank-you.html` (Show prize/confirmation)

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
   - **Maynaguri**: `https://your-domain.github.io/TSC-QR-Reward-System/?store=MNG`
   - **Dhupguri**: `https://your-domain.github.io/TSC-QR-Reward-System/?store=DPG`
   - **Jamaldaha**: `https://your-domain.github.io/TSC-QR-Reward-System/?store=JMD`

### 📱 QR Code Flow
Customers scan QR → `index.html?store=MNG` → Click "Get Started" → `welcome.html?store=MNG` → Choose reward → Complete tasks/tokens → Success!

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

---

## 👨‍💻 Developer & Credits

- **Lead Developer**: PsProsen-Dev
- **Framework**: RTX Protocol v1.5
- **Engine**: Claude Sonnet 4 + VS Code Integration
- **Design**: Gold Royal Luxe, glassmorphism, mobile-first
- **Branding**: The Shankar Communications (TSC)

---

## 📞 Support

- 📧 Email: support@tsc-tech.com
- 📱 WhatsApp: +91 98765 43210
- 🌐 Website: https://tsc-tech.com

---

**Made with ❤️ for The Shankar Communications (TSC)**

*Empowering customer engagement through innovative QR reward systems* 🎯🚀
