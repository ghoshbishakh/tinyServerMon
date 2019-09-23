#!/usr/bin/env bash
du -sx $1 | sed "s/[ \t]\+/ /g" > users_space.txt
chmod 555 users_space.txt