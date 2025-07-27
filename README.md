# The Shankar Communications (TSC) QR Reward System

🏪 **Unified QR Code Reward System for The Shankar Communications**

A mobile-first web application providing interactive rewards and offers for customers visiting The Shankar Communications (TSC) stores via QR code scanning. All branding follows the format:

```
The Shankar Communications
(TSC)
[Section/Context]
```

## 🌟 Features

### 🎡 Spin & Win System
- Interactive spinning wheel with 8+ prizes
- Task-based unlock (Instagram, YouTube, Google reviews, WhatsApp group)
- Progress tracking with localStorage
- One-time spin per session

### 🛡️ Tempered Glass ₹19 Offer
- Special discounted offer system
- Token-based verification (local/external)
- WhatsApp integration for token generation
- Cross-store token validation

### 🏪 Multi-Store Support
- **Maynaguri (MNG)** - `?store=MNG`
- **Dhupguri (DPG)** - `?store=DPG`
- **Jamaldaha (JMD)** - `?store=JMD`

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

## 🚦 Main Flows

### 🎡 Spin & Win Flow
1. **Entry** → `welcome.html?store=MNG`
2. **Choose Spin & Win**
3. **Tasks** → `tasks-new.html` (Complete 4 social tasks)
4. **Reward** → `reward.html` (Spin the wheel)
5. **Success** → `thank-you.html` (Show prize details)

### 🛡️ Tempered Glass Flow
1. **Entry** → `welcome.html?store=MNG`
2. **Choose Tempered Glass**
3. **Offer** → `tempered-glass.html` (Token entry or generation)
4. **Generate** → `generate-token.html` or store-specific token page
5. **Success** → `thank-you.html` (Token verified)

## 🔧 Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (all inline)
- **Styling**: Glassmorphism, gradients, mobile-first responsive
- **Storage**: localStorage for progress tracking
- **Hosting**: GitHub Pages
- **Integration**: WhatsApp Web API for messaging

## 🎨 Design Features

- **Mobile-First**: Optimized for smartphones
- **Glassmorphism**: Modern frosted glass UI effects
- **Gradient Backgrounds**: Eye-catching color schemes
- **Responsive**: Works on all screen sizes
- **Accessibility**: High contrast, readable fonts
- **Animations**: Smooth transitions and micro-interactions
- **Branding**: All customer-facing places use:
  - The Shankar Communications<br>(TSC)<br>[Section/Context]

## 🛠️ Setup & Deployment

### 1. GitHub Repository Setup
```bash
git clone https://github.com/your-username/TSC-QR-Reward-System.git
cd TSC-QR-Reward-System
```

### 2. Local Development
```bash
# Serve locally (Python)
python -m http.server 8000
# Or use Live Server in VS Code
# Visit: http://localhost:8000/?store=MNG
```

### 3. GitHub Pages Deployment
1. Go to repository → Settings → Pages
2. Source: Deploy from branch → `main` → `/root`
3. Save and wait for deployment
4. Access via: `https://your-username.github.io/TSC-QR-Reward-System/`

### 4. QR Code Generation
Generate QR codes for each store URL:
```
Store MNG: https://your-username.github.io/TSC-QR-Reward-System/?store=MNG
Store DPG: https://your-username.github.io/TSC-QR-Reward-System/?store=DPG  
Store JMD: https://your-username.github.io/TSC-QR-Reward-System/?store=JMD
```

## ⚙️ Customization

### Update Store Information
Edit the store objects in each HTML file:
```javascript
const storeInfo = {
    'MNG': 'Maynaguri Branch',
    'DPG': 'Dhupguri Branch', 
    'JMD': 'Jamaldaha Branch'
};
```

### Modify Prizes
Edit `reward.html` prizes array:
```javascript
const prizes = [
    { text: "10% OFF", emoji: "🎁", description: "Get 10% discount!" },
    // Add/modify prizes here
];
```

### Update Social Links
Edit task links in `tasks-new.html`:
```javascript
// Instagram, YouTube, Google Reviews, WhatsApp Group URLs
```

## 📊 Analytics & Tracking

### LocalStorage Data Tracked
- `currentStore`: Selected store (MNG/DPG/JMD)
- `completedTasks`: Array of completed social tasks
- `hasSpun`: Boolean for spin wheel usage
- `wonPrize`: Prize object from spin result
- `verifiedToken`: Successfully verified token
- `tokenType`: 'local' or 'external' token type

### Usage Monitoring
Monitor user engagement through:
- Task completion rates
- Spin wheel usage
- Token generation requests
- Store visit patterns

## 🚀 Future Enhancements

- [ ] **Backend Integration**: User accounts, analytics dashboard
- [ ] **Push Notifications**: Remind users about unused rewards
- [ ] **Geolocation**: Verify users are actually at store locations
- [ ] **Advanced Tokens**: Time-limited, usage-limited tokens
- [ ] **Social Sharing**: Auto-post rewards to social media
- [ ] **Multi-language**: Hindi/Bengali language support
- [ ] **Admin Panel**: Store staff interface for token management

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**PsProsen-Dev** 💻✨
- Framework: RTX Protocol v1.5
- Engine: Claude Sonnet 4 + VS Code Integration

## 📞 Support

For technical support or customization requests:
- 📧 Email: support@tsc-tech.com
- 📱 WhatsApp: +91 98765 43210
- 🌐 Website: https://tsc-tech.com

---

**Made with ❤️ for The Shankar Communications (TSC)**

*Empowering customer engagement through innovative QR reward systems* 🎯🚀
