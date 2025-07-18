from tutor import hooks
import os
from os.path import basename

SN_PATH = os.path.abspath("env/build/openedx/requirements/git-reqs/sn-edx-middleware")

hooks.Filters.IMAGES_BUILD_MOUNTS.add_item(("sn-edx-middleware", SN_PATH))
hooks.Filters.COMPOSE_MOUNTS.add_item(("openedx", "/mnt/sn-edx-middleware"))
    


hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", SN_PATH))


private_package_paths = [
    "./requirements/git-reqs/sn-edx-middleware",
]

# hooks.Filters.ENV_PATCHES.add_item(
#     (
#         "openedx-dockerfile-post-python-requirements",
#         "\n".join([f"""
# COPY --chown=app:app {path} /mnt/{basename(path)}
# RUN pip install -e /mnt/{basename(path)}
# """ for path in private_package_paths])
#     )
# )

