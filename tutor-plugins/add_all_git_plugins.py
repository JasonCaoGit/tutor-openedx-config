# from tutor import hooks
# import glob
# import os
# from os.path import basename, abspath

# # Update this to your actual git-reqs directory:
# GIT_REQS_DIR = "requirements/git-reqs"
# if os.path.isdir(GIT_REQS_DIR):
#     private_paths = [
#         os.path.join(GIT_REQS_DIR, d)
#         for d in os.listdir(GIT_REQS_DIR)
#         if os.path.isdir(os.path.join(GIT_REQS_DIR, d))
#     ]
# else:
#     private_paths = []


# # Absolute path to your local middleware directory


# print(private_paths)

# # Reconstruct the path forms for the build mounts
# name_patterns = [
#     ("openedx", r".*%s$" % basename(p)) for p in private_paths
# ]
# hooks.Filters.MOUNTED_DIRECTORIES.apply(name_patterns)

# # hooks.Filters.MOUNTED_DIRECTORIES(name_patterns)



# # Enable plugins inside the openedx container
# hooks.Filters.ENV_PATCHES.add_item(
#     (
#         "openedx-dockerfile-post-python-requirements",
#         "\n".join([f"""
# COPY --chown=app:app {path} /mnt/{basename(path)}
# RUN pip install -e /mnt/{basename(path)}
# """ for path in private_paths])
#     )
# )

# middleware_path = "sn_edx_middleware.middleware.SkillsNetworkEdxMiddleware"

# hooks.Filters.ENV_PATCHES.add_items([
#     ("lms-env", "EXTRA_MIDDLEWARE:"),
#     ("lms-env", "  - sn_edx_middleware.middleware.SkillsNetworkEdxMiddleware"),
#     ("cms-env", "EXTRA_MIDDLEWARE:"),
#     ("cms-env", "  - sn_edx_middleware.middleware.SkillsNetworkEdxMiddleware"),
# ])