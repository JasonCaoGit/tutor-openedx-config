
# Project Setup

To get started with the development environment:

## Prerequisites

### Rancher Desktop Setup

**Pricing**: Free and open source (Apache 2.0).

**Installation**:
1. Download the appropriate version for your operating system from [Rancher Desktop by SUSE](https://rancherdesktop.io/)
2. Open the downloaded installer and drag the app to the Applications folder
3. Run the Rancher Desktop application and in the setup dialog choose the defaults as of this writing:
   - Enable the latest stable Kubernetes
   - The dockerd (moby) Container Engine
   - Automatic path configuration

**Configuration**:
1. Under **Settings → Virtual Machine → Hardware**, increase Memory to 8GB
2. Under **Settings → Virtual Machine → Emulation**, select VZ and Enable Rosetta Support
3. Under **Settings → Virtual Machine → Volumes**, select virtiofs
4. Click the button to **Apply** the settings changes

## Development Environment Setup

1. **Load environment variables**

   ```bash
   source .env
   ```

2. **Install Tutor**

   Make sure you have Python and pip installed, then run:

   ```bash
   pip install tutor
   ```

3. **Start Tutor in development mode**

   ```bash
   tutor dev launch
   ```

