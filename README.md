# 🏪 The Shankar Communications (TSC) QR Reward System

**Unified QR Code-Based Customer Engagement Platform**

A comprehensive mobile-first web application providing interactive rewards, loyalty programs, and promotional offers for customers visiting The Shankar Communications (TSC) stores through QR code scanning. Features sophisticated branding consistency, multi-store support, and seamless social media integration.

## 🎯 **System Overview**

The TSC QR Reward System is a customer engagement platform that provides two primary reward pathways:
- **🎡 Spin & Win Game**: Task-based rewards with social media engagement
- **🛡️ Tempered Glass Offer**: Special ₹19 promotional offer with token verification

All customer-facing content maintains consistent branding format:
```
The Shankar Communications
(TSC)
[Context/Section]
```

## 🌟 **Core Features**

### 🎮 **Interactive Reward System**
- **Spin & Win Wheel**: 8-segment wheel with physical prizes (Botel, Earbuds, Neckband, Mobile Stand)
- **Social Media Integration**: 6 engagement tasks across platforms
- **Progress Tracking**: Real-time task completion monitoring
- **One-Time Rewards**: Session-based limitations to prevent abuse

### 🛡️ **Tempered Glass Promotion**
- **₹19 Special Offer**: Premium screen protector at promotional price
- **Token-Based Verification**: Secure validation system
- **WhatsApp Integration**: Automated token generation and delivery
- **Multi-Store Support**: Store-specific token generation

### 🏪 **Multi-Store Architecture**
- **Maynaguri Store (MNG)**: `?store=MNG`
- **Dhupguri Store (DPG)**: `?store=DPG` 
- **Jamaldaha Store (JMD)**: `?store=JMD`

### 🎨 **Modern UI/UX Design**
- **RTX-Inspired Theme**: Premium golden color scheme (#FFD700)
- **Glassmorphism Effects**: Modern frosted glass UI components
- **Mobile-First Design**: Optimized for smartphone usage
- **Responsive Layout**: Adaptive across all screen sizes
- **Smooth Animations**: Enhanced user experience with micro-interactions

## 📁 **Project Architecture**

```
TSC-QR-Reward-System/
│
├── 🏠 MAIN PAGES
│   ├── index.html                    # Loyalty landing page (store-specific entry)
│   ├── welcome.html                  # Unified reward center (choose path)
│   └── thank-you.html                # Success/completion confirmation
│
├── 🎡 SPIN & WIN SYSTEM
│   ├── tasks-new.html                # Social media task completion
│   └── reward.html                   # Interactive spinning wheel
│
├── 🛡️ TEMPERED GLASS SYSTEM
│   ├── tempered-glass.html           # Offer presentation & token entry
│   ├── generate-token.html           # Generic WhatsApp token generation
│   ├── generate-token-mng.html       # Maynaguri-specific token generator
│   ├── generate-token-dpg.html       # Dhupguri-specific token generator
│   └── generate-token-jmd.html       # Jamaldaha-specific token generator
│
├── 🔧 ADMIN & UTILITIES
│   ├── decode-token.html             # Token validation & management
│   └── token-generator-advanced.html # Advanced admin token tools
│
└── 🖼️ ASSETS
    ├── tsc-logo.jpg                  # Official TSC branding logo
    ├── temp_files.txt                # Development backup files
    └── README.md                     # Project documentation
```

## 🔄 **User Journey Flows**

### 🎡 **Spin & Win Customer Journey**
```
QR Scan → Store Landing → Welcome Page → Choose "Spin & Win" 
    ↓
Social Tasks Page → Complete 6 Tasks → Unlock Spin Wheel
    ↓
Spin Wheel → Win Prize → Success Page → Share/Collect
```

**Required Tasks (6 total):**
1. 📱 WhatsApp Join (`+917908972637`)
2. 📢 WhatsApp Channel Follow
3. ⭐ Google Review Submission
4. 👥 Facebook Page Follow
5. 📸 Instagram Account Follow  
6. 🎥 YouTube Channel Subscribe

### 🛡️ **Tempered Glass Offer Journey**
```
QR Scan → Store Landing → Welcome Page → Choose "Tempered Glass"
    ↓
Option Selection: [Have Token] OR [Generate New Token]
    ↓
Token Entry → Validation → Success Page → Claim Instructions
```

## 🛠️ **Technical Implementation**

### **Frontend Stack**
- **HTML5**: Semantic structure with modern standards
- **CSS3**: Advanced styling with glassmorphism, gradients, animations
- **Vanilla JavaScript**: Client-side interactivity and state management
- **FontAwesome 6.5**: Comprehensive icon library
- **Google Fonts**: Poppins typography family

### **Storage & State Management**
- **localStorage**: Persistent client-side data storage
- **Session Management**: Task completion tracking
- **Cross-Page Data**: Store selection and progress sharing

### **Responsive Design**
```css
/* Mobile-First Breakpoints */
@media (max-width: 480px)  { /* Small phones */ }
@media (max-width: 768px)  { /* Tablets & large phones */ }
@media (min-width: 769px)  { /* Desktop & laptops */ }
```

### **Performance Optimizations**
- **Inline CSS/JS**: Reduced HTTP requests
- **Optimized Images**: Compressed assets
- **Efficient Animations**: GPU-accelerated transforms
- **Minimal Dependencies**: Lightweight external libraries

## 🎨 **Design System & Branding**

### **Color Palette**
```css
Primary Gold: #FFD700     /* Main branding color */
Dark Gradient: #0a0a0a → #1a1a1a → #0a0a0a
Accent Green: #00ff7f     /* Tempered glass theme */
Status Colors: #4ECDC4, #FF6B6B, #96CEB4, #45B7D1
```

### **Typography**
```css
Font Family: 'Poppins', sans-serif
Weights: 400 (Regular), 600 (Semi-Bold), 700 (Bold)
Hierarchy: 28px (H1) → 22px (H2) → 16px (Body) → 14px (Small)
```

### **Consistent Branding**
All customer-facing elements display:
```
The Shankar Communications
(TSC)  
[Relevant Context]
```

## ⚙️ **Configuration & Customization**

### **Store Information Update**
Edit store configurations in each HTML file:
```javascript
const storeInfo = {
    'MNG': 'Maynaguri Store',
    'DPG': 'Dhupguri Store',
    'JMD': 'Jamaldaha Store'
};
```

### **Prize Configuration** (`reward.html`)
```javascript
const prizes = [
    { text: 'Botel', color: '#FF6B6B', weight: 20 },
    { text: 'Earbuds', color: '#4ECDC4', weight: 25 },
    { text: 'Neckband', color: '#45B7D1', weight: 30 },
    { text: 'Mobile Stand', color: '#96CEB4', weight: 25 }
];
```

### **Social Media Links** (`tasks-new.html`)
```javascript
// WhatsApp: https://wa.me/917908972637
// Channel: https://whatsapp.com/channel/0029VbAoFCtAe5VmITgCtN0E
// Facebook: https://facebook.com/theshankarcommunications
// Instagram: https://instagram.com/theshankarcommunications
// YouTube: [Configure as needed]
// Google Reviews: [Store-specific Google Business links]
```

## 🚀 **Deployment & Setup**

### **1. Repository Setup**
```bash
git clone https://github.com/PsProsen-Dev/TSC-QR-Reward-System.git
cd TSC-QR-Reward-System
```

### **2. Local Development**
```bash
# Using Python HTTP Server
python -m http.server 8000

# Using Node.js HTTP Server  
npx http-server -p 8000

# Using VS Code Live Server Extension
# Right-click index.html → "Open with Live Server"

# Access: http://localhost:8000/?store=MNG
```

### **3. GitHub Pages Deployment**
1. Navigate to repository **Settings** → **Pages**
2. Source: **Deploy from branch** → `master` → `/ (root)`
3. Save and wait for automated deployment
4. Access via: `https://psprosen-dev.github.io/TSC-QR-Reward-System/`

### **4. QR Code Generation**
Create QR codes for each store entry point:
```
MNG Store: https://psprosen-dev.github.io/TSC-QR-Reward-System/?store=MNG
DPG Store: https://psprosen-dev.github.io/TSC-QR-Reward-System/?store=DPG  
JMD Store: https://psprosen-dev.github.io/TSC-QR-Reward-System/?store=JMD
```

## 📊 **Analytics & Data Tracking**

### **localStorage Data Schema**
```javascript
// Store Selection
currentStore: "MNG" | "DPG" | "JMD"

// Task Completion (Spin & Win)
whatsapp_done: "true" | null
channel_done: "true" | null  
review_done: "true" | null
fb_done: "true" | null
insta_done: "true" | null
yt_done: "true" | null

// Timestamp Tracking
[task]_timestamp: ISO 8601 DateTime

// Reward System
hasSpun: "true" | null
wonPrize: JSON Prize Object
flow_type: "spin" | "tg" | "tg_generate"

// Token Management
spin_token: "4-digit-code"
tg_token: "4-digit-code"  
token_digits: "4-digit-code"
```

### **Usage Monitoring Opportunities**
- Task completion rates by store
- Most popular reward path (Spin vs Tempered Glass)
- Social media engagement effectiveness
- Token generation and redemption patterns
- Mobile vs desktop usage analytics

## 🔮 **Future Enhancement Roadmap**

### **Phase 1: Backend Integration**
- [ ] **User Accounts**: Registration and login system
- [ ] **Database**: User data and analytics storage
- [ ] **Admin Dashboard**: Store management interface
- [ ] **API Integration**: Real-time data synchronization

### **Phase 2: Advanced Features**
- [ ] **Geolocation Verification**: Ensure users are at physical stores
- [ ] **Time-Limited Tokens**: Enhanced security with expiration
- [ ] **Push Notifications**: Remind users about unclaimed rewards
- [ ] **Social Sharing**: Auto-post achievements to social media

### **Phase 3: Regional Expansion**
- [ ] **Multi-Language Support**: Hindi, Bengali language options
- [ ] **Regional Customization**: Local festival and cultural content
- [ ] **Franchise Support**: Multi-business management capabilities
- [ ] **Advanced Analytics**: Business intelligence and reporting

### **Phase 4: Technology Upgrades**
- [ ] **PWA Implementation**: Progressive Web App features
- [ ] **Offline Support**: Cached content and offline task tracking
- [ ] **AI Integration**: Personalized recommendations and chatbot
- [ ] **Blockchain Tokens**: Secure, tradeable reward tokens

## 🛡️ **Security & Best Practices**

### **Client-Side Security**
- Input validation for all user entries
- XSS prevention in dynamic content
- Secure localStorage usage patterns
- HTTPS enforcement for production

### **Token Security**
- 4-digit numeric tokens for simplicity
- Session-based validation
- Store-specific token generation
- Timestamp tracking for audit trails

## 🤝 **Contributing Guidelines**

### **Development Workflow**
1. **Fork** the repository
2. **Create feature branch**: `git checkout -b feature/enhancement-name`
3. **Commit changes**: `git commit -am 'Add new feature: description'`
4. **Push to branch**: `git push origin feature/enhancement-name`
5. **Create Pull Request** with detailed description

### **Code Standards**
- Maintain consistent indentation (2 spaces)
- Use semantic HTML5 elements
- Follow mobile-first CSS approach
- Comment complex JavaScript logic
- Preserve RTX theme consistency

### **Testing Checklist**
- [ ] Test on multiple mobile devices
- [ ] Verify all QR code entry points
- [ ] Validate social media link functionality
- [ ] Confirm token generation and validation
- [ ] Check cross-browser compatibility

## 📄 **Licensing & Credits**

### **Project License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### **Technology Credits**
- **Framework**: RTX Protocol v1.5 (Custom Development Framework)
- **AI Development**: Claude Sonnet 4 + ChatGPT Integration  
- **IDE Integration**: VS Code with AI-powered assistance
- **Design System**: Gold Royal Luxe Theme

### **Development Team**
**Lead Developer**: **Prosenjit Paul (Ps Prosen)**
- 🌐 Portfolio: [psprosen.me](https://psprosen.me)
- 💼 GitHub: [@PsProsen-Dev](https://github.com/PsProsen-Dev)
- 🏢 Studio: [We Digital Mitra](https://we-digital-mitra.tech)

## 📞 **Support & Contact**

### **Technical Support**
For customization requests, bug reports, or feature suggestions:

- 📧 **Email**: support@we-digital-mitra.tech
- 💬 **WhatsApp**: +91 79089 72637
- 🌐 **Website**: [we-digital-mitra.tech](https://we-digital-mitra.tech)
- 🐛 **Issues**: [GitHub Issues](https://github.com/PsProsen-Dev/TSC-QR-Reward-System/issues)

### **Business Inquiries**
For similar system development or business partnerships:

- 📞 **Phone**: +91 79089 72637
- 📧 **Business Email**: business@we-digital-mitra.tech
- 💼 **LinkedIn**: [Connect with Ps Prosen](https://linkedin.com/in/prosenjitpaul)

---

## 🏆 **Project Achievements**

✅ **Mobile-First Design** - Optimized smartphone experience  
✅ **Multi-Store Architecture** - Scalable business model  
✅ **Social Media Integration** - Enhanced customer engagement  
✅ **Token-Based Security** - Secure reward validation  
✅ **RTX Theme Implementation** - Premium visual experience  
✅ **Zero-Backend Deployment** - Cost-effective hosting solution  
✅ **Real-Time Progress Tracking** - Enhanced user experience  

---

**Made with ❤️ for The Shankar Communications (TSC)**

*Revolutionizing customer engagement through innovative QR-based reward systems* 🎯✨

**© 2025 We Digital Mitra | Developed by Ps Prosen**
