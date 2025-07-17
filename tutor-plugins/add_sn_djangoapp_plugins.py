from tutor import hooks
from os.path import basename

private_package_paths = [
    "./requirements/git-reqs/sn-edx-middleware", 
]

hooks.Filters.ENV_PATCHES.add_item(
    ("openedx-dockerfile-post-python-requirements",
    "\n".join(

        [
            f"""
            COPY --chown=app:app {path} /mnt/{basename(path)}
            RUN pip install -e /mnt/{basename(path)}
            """ for path in private_package_paths
        ]
    ))

)