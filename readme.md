
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

1. **Clone the repository with submodules**

   > **Important:** This project uses git submodules. To ensure all dependencies are present, clone with the `--recursive` flag:
   >
   > ```bash
   > git clone --recursive <repository-url-to-this-repo>
   > ```



2. **Load environment variables**

   ```bash
   source .env
   ```

3. **Install Tutor**

   Make sure you have Python and pip installed, then run:

   ```bash
   pip install tutor
   ```

4. **Start Tutor in development mode**

   ```bash
   tutor dev launch
   ```


# How to Add Middleware (Hot-Reloaded)

This guide will help you add new middleware to your Open edX development environment. All middleware placed in `env/build/openedx/requirements/git-reqs/` will be hot-reloaded automatically inside your Tutor containers.

## Step 1: Add the Middleware as a Git Submodule

First, add your middleware repository as a submodule inside the `git-reqs` directory. This keeps your dependencies organized and up-to-date.

```bash
# Example: Add the sn-edx-middleware repo as a submodule
cd env/build/openedx/requirements/git-reqs

git submodule add https://github.com/ibm-skills-network/<your-repo>.git

# You can repeat this for any other middleware you want to add
```

## Step 2: Load Environment Variables

Before running any Tutor commands, make sure your environment variables are loaded:

```bash
source .env
```

## Step 3: Enable the Middleware Mounting Plugin

Enable the plugin that will automatically mount all middleware folders for you, because our plugins are custom, we need add it to MOUNTED_DIRECTORIES explicitly:

```bash
tutor plugins enable add_all_middlewares.py
```

This plugin will ensure that every folder in `git-reqs` is recognized and mounted by Tutor, when we run git mounts add <path-to-custom-middleware>.

## Step 4: Mount All Middleware Folders

Run the provided script to add all middleware folders as Tutor mounts:

```bash
scripts/mount_all_middlewares.sh
```

This script will:
- Loop through every folder in `git-reqs`
- Add each as a mount using Tutor

## Step 5: Launch Tutor in Development Mode

Start your Tutor environment in development mode:

```bash
tutor dev launch
```

## Result: Hot Reloading

All files in `env/build/openedx/requirements/git-reqs/` will now be hot-loaded into your Tutor containers. Don't need to re-build the image. Any changes you make will be instantly reflected inside the running Open edX environment.

---

**Tip:**
- If you add new middleware folders later, just repeat steps 1 and 4.
- You can check which folders are mounted with `tutor mounts list`.

