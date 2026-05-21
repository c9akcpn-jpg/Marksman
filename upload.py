import os
import shutil
import subprocess

# ========= CONFIG =========
TOKEN = os.getenv("GITHUB_TOKEN")

USERNAME = "c9akcpn-jpg"
REPO_NAME = "Marksman"

SOURCE_FOLDER = "zips"
TXT_FILE = "links.txt"

CURRENT_DIR = os.getcwd()

# keep .git cache for speed
REPO_DIR = os.path.join(CURRENT_DIR, ".temp_repo")

REPO_URL = f"https://{USERNAME}:{TOKEN}@github.com/{USERNAME}/{REPO_NAME}.git"


# ========= FAST RUN =========
def run(cmd, cwd=None):

    return subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


# ========= MAIN =========
def upload_all_zip():

    # ===== TOKEN =====
    if not TOKEN:
        print("❌ GITHUB_TOKEN not set")
        return

    # ===== ZIP FOLDER =====
    if not os.path.exists(SOURCE_FOLDER):
        os.makedirs(SOURCE_FOLDER)
        print("📁 zips folder created")
        return

    # ===== GET ZIPS =====
    zip_files = [
        f for f in os.listdir(SOURCE_FOLDER)
        if f.endswith(".zip")
    ]

    if not zip_files:
        print("❌ No zip files found")
        return

    print(f"📦 Found {len(zip_files)} zip files")

    # ===== GIT CONFIG =====
    run('git config --global user.email "bot@example.com"')
    run('git config --global user.name "AutoBot"')

    # ===== FIRST CLONE ONLY =====
    if not os.path.exists(REPO_DIR):

        print("📥 First clone...")

        clone = run(
            f"git clone --depth 1 {REPO_URL} {REPO_DIR}"
        )

        if clone.returncode != 0:
            print("❌ Clone failed")
            return

    else:

        print("⚡ Fast update...")

        # reset repo fast
        run("git reset --hard", cwd=REPO_DIR)

        # pull latest only
        pull = run("git pull", cwd=REPO_DIR)

        if pull.returncode != 0:
            print("❌ Pull failed")
            return

    # ===== REMOVE OLD ZIPS =====
    print("🗑 Cleaning old zip files...")

    for file in os.listdir(REPO_DIR):

        if file.endswith(".zip"):

            try:
                os.remove(os.path.join(REPO_DIR, file))
            except:
                pass

    # ===== COPY NEW FILES =====
    print("📋 Copying files...")

    for file in zip_files:

        src = os.path.join(SOURCE_FOLDER, file)

        dst = os.path.join(REPO_DIR, file)

        shutil.copy2(src, dst)

        print(f"✔ {file}")

    # ===== GIT PUSH =====
    print("🚀 Uploading...")

    run("git add .", cwd=REPO_DIR)

    run(
        'git commit -m "Auto upload zip"',
        cwd=REPO_DIR
    )

    push = run("git push", cwd=REPO_DIR)

    if push.returncode == 0:
        print("✅ Upload success")
    else:
        print("❌ Push failed")
        return

    # ===== GENERATE LINKS =====
    print("🔗 Generating links...")

    with open(TXT_FILE, "w") as f:

        for file in zip_files:

            link = (
                f"https://raw.githubusercontent.com/"
                f"{USERNAME}/{REPO_NAME}/main/{file}"
            )

            f.write(link + "\n")

            print(link)

    print("✅ links.txt saved")

    # ===== CLEAN ZIPS ONLY =====
    print("🧹 Removing temp zip files...")

    for file in os.listdir(REPO_DIR):

        if file.endswith(".zip"):

            try:
                os.remove(os.path.join(REPO_DIR, file))
            except:
                pass

    print("✅ Cleanup complete")


# ========= START =========
if __name__ == "__main__":
    upload_all_zip()