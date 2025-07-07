# Tutor Configuration Repository

This repository contains **Tutor configuration files** for OpenEdX deployment. It's designed to save and version control your Tutor setup, not the actual OpenEdX application.

## 📋 Purpose

This repo is for:
- ✅ **Saving Tutor configuration** (`config.yml`)
- ✅ **Version controlling environment settings** (`env/`)
- ✅ **Sharing Tutor customizations** between team members
- ❌ **NOT for storing OpenEdX data** (databases, media files, etc.)

## 📁 What's Tracked

```
tutor-openedx-config/
├── config.yml                 # Main Tutor configuration
├── env/                       # Environment configurations
│   ├── build/                # Docker build customizations
│   ├── local/                # Local development settings
│   └── plugins/              # Custom plugins
├── data/                     # Data directories (gitignored)
├── tutor-config-vanilla/     # Vanilla Tutor config
└── README.md                 # This file
```

## 🚀 Usage

### 1. **Save your Tutor config**:
```bash
tutor config save
```

### 2. **Commit changes**:
```bash
git add config.yml env/
git commit -m "Update Tutor configuration"
```

### 3. **Share with team**:
```bash
git push origin main
```

## ⚙️ Configuration Files

### `config.yml`
- **OpenEdX version** and release
- **Domain settings**
- **Plugin configurations**
- **Resource allocations**

### `env/` Directory
- **Build optimizations** for Rancher Desktop
- **Custom Docker configurations**
- **Plugin customizations**

## 🔧 Customizations

### For Rancher Desktop Issues
The `env/build/openedx/Dockerfile` includes:
- **Memory optimizations** for webpack builds
- **Network retry logic** for pip installs
- **Timeout configurations** for corporate networks

### Adding Custom Plugins
1. Create plugin in `env/plugins/`
2. Update `config.yml` to enable it
3. Commit the changes

## 🐛 Common Issues

### Build Problems
- **Webpack hanging**: Check memory allocation in Rancher
- **Network timeouts**: Use retry logic in Dockerfile
- **Memory issues**: Increase Rancher VM resources

### IBM Corporate Environment
- **Use Rancher Desktop** (Docker Desktop blocked)
- **Configure for corporate firewall**
- **Optimize for network restrictions**

## 📝 Best Practices

1. **Never commit sensitive data**:
   - Database credentials
   - API keys
   - SSL certificates

2. **Always commit configuration changes**:
   - `config.yml` updates
   - `env/` customizations
   - Plugin configurations

3. **Use meaningful commit messages**:
   ```bash
   git commit -m "Add MFE plugin configuration"
   git commit -m "Optimize webpack build for Rancher"
   ```

## 🤝 Team Workflow

1. **Clone the repo** to get Tutor config
2. **Run `tutor config save`** to apply config
3. **Make changes** to `config.yml` or `env/`
4. **Commit and push** changes
5. **Team members pull** and apply updates

---

**Note**: This repository is specifically for Tutor configuration management in IBM corporate environments using Rancher Desktop.