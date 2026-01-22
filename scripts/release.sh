#!/usr/bin/env bash
#
# Release the project and bump version number in the process.
# source: https://slhck.info/software/2025/10/01/dynamic-versioning-uv-projects.html

set -e

# change to project root
cd "$(dirname "$(dirname "$0")")"

usage() {
    echo "Usage: $0 [options] VERSION"
    echo
    echo "VERSION:"
    echo "  major: bump major version number"
    echo "  minor: bump minor version number"
    echo "  patch: bump patch version number"
    echo "  pre_l: bump pre-release label"
    echo "  pre_n: pre-release version number (default)"
    echo
    echo "Options:"
    echo "  -h, --help:   show this help message"
    exit 1
}

# parse args
while [ "$#" -gt 0 ]; do
    case "$1" in
    -h | --help)
        usage
        ;;
    *)
        break
        ;;
    esac
done

# check if version is specified
if [ "$#" -ne 1 ]; then
    VERSION="pre_n"
  else
    VERSION=$1
fi

if [ "$VERSION" != "major" ] && [ "$VERSION" != "minor" ] && [ "$VERSION" != "patch" ] && [ "$VERSION" != "pre_l" ] && [ "$VERSION" != "pre_n" ] ; then
    usage
fi

# should commit be tagged? infer from version-bump
TAG_COMMIT=0
if [ $VERSION != "pre_n" ] || [ $VERSION != "pre_l" ]; then
    TAG_COMMIT=1
fi


if ! command -v bump-my-version &> /dev/null; then
    echo "Error: bump-my-version is not installed. Please run `pip install bump-my-version`"
    exit 1
fi

echo "Would bump version:"
bump-my-version show --increment $VERSION new_version


# save git message
# git log -1 --pretty=%B > /tmp/msg.txt
# only run commit-msg hook (to run changelog-helper)
# pre-commit run --hook-stage commit-msg --commit-msg-file /tmp/msg.txt
# run post-commit stage to generate changelog with new commit tag included
# pre-commit run --hook-stage post-commit
