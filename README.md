# TSC QR Reward System

🏪 **Unified QR Code Reward System for TSC (Technology Service Center)**

A mobile-first web application that provides interactive rewards and offers for customers visiting TSC's physical stores through QR code scanning.

## 🚀 Live Demo

**Main Entry Point:** https://psprosen-dev.github.io/TSC-QR-Reward-System/

**Store-specific URLs:**
- 🏪 **Maynaguri:** https://psprosen-dev.github.io/TSC-QR-Reward-System/?store=MNG
- 🏪 **Dhupguri:** https://psprosen-dev.github.io/TSC-QR-Reward-System/?store=DPG  
- 🏪 **Jamaldaha:** https://psprosen-dev.github.io/TSC-QR-Reward-System/?store=JMD

## 🌟 Features

- 🎰 **Spin & Win System** - Interactive spinning wheel with physical prizes
- 🏪 **Multi-Store Support** - Separate experiences for each TSC location
- 📱 **Mobile-First Design** - Optimized for smartphone usage
- 🎨 **Premium UI** - Modern glassmorphism design with smooth animations
- 💾 **Progress Tracking** - localStorage-based session management
- 📞 **WhatsApp Integration** - Direct token generation and verification

## 🎁 Current Prizes

- **Botel** (20% chance)
- **Earbuds** (25% chance)
- **Neckband** (30% chance)
- **Mobile Stand** (25% chance)

## 🔧 Technical Stack

- **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Styling:** CSS Grid/Flexbox, Mobile-first responsive design
- **Storage:** localStorage for progress tracking
- **Hosting:** GitHub Pages
- **Integration:** WhatsApp Web API for messaging

## 👨‍💻 Developer

**Crafted by [Ps Prosen](https://psprosen.me) | Powered by [WDM](https://we-digital-mitra.tech)**

---

*Made with ❤️ for TSC Technology Service Centers*

## 🔧 Technical Stack

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid/Flexbox, Mobile-first responsive design
- **Storage**: localStorage for progress tracking
- **Hosting**: GitHub Pages
- **Integration**: WhatsApp Web API for messaging

## 🎯 User Journey

### 🎡 Spin & Win Flow
1. **Entry** → `index.html?store=MNG`
2. **Tasks** → `tasks.html` (Complete 4 social tasks)
3. **Reward** → `reward.html` (Spin the wheel)
4. **Success** → `thank-you.html` (Show prize details)

### 🛡️ Tempered Glass Flow
1. **Entry** → `index.html?store=MNG`
2. **Offer** → `tempered-glass.html` (Token entry or generation)
3. **Generate** → `generate-token.html` (WhatsApp verification)
4. **Success** → `thank-you.html` (Token verified)

## 🔐 Token System

### Local Store Tokens
```javascript
MNG: ['MNG-1-24', 'MNG-2-24', 'MNG-3-24']
DPG: ['DPG-1-24', 'DPG-2-24', 'DPG-3-24'] 
JMD: ['JMD-1-24', 'JMD-2-24', 'JMD-3-24']
```

### External/Cross-Store Tokens
```javascript
['MNG3-TSC5-TG3', '07-TSC-25', 'TG-1911']
```

## 📱 WhatsApp Integration

### Message Template
```
Hi TSC, I'm at your [STORE_NAME] branch to claim the ₹19 Tempered Glass offer. Please verify me.
```

### Store Phone Numbers (Update these)
```javascript
const storePhoneNumbers = {
    'MNG': '919876543210', // Maynaguri
    'DPG': '919876543211', // Dhupguri  
    'JMD': '919876543212'  // Jamaldaha
};
```

## 🎨 Design Features

- **Mobile-First**: Optimized for smartphones
- **Glassmorphism**: Modern frosted glass UI effects
- **Gradient Backgrounds**: Eye-catching color schemes
- **Responsive**: Works on all screen sizes
- **Accessibility**: High contrast, readable fonts
- **Animations**: Smooth transitions and micro-interactions

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
Edit task links in `tasks.html`:
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

**Made with ❤️ for TSC Technology Service Centers**

*Empowering customer engagement through innovative QR reward systems* 🎯🚀
