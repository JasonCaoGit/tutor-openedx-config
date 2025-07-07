#! /bin/sh
setowner $OPENEDX_USER_ID /mounts/lms /mounts/cms /mounts/openedx
setowner 1000 /mounts/meilisearch
setowner 999 /mounts/mongodb
setowner 999 /mounts/mysql
setowner 1000 /mounts/redis

