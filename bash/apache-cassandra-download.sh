#!/bin/bash

usage() {
  echo "Usage: $0 [-d|-r] -v <version> [-l <location>]"
  echo "  -d: debian"
  echo "  -r: redhat"
  echo "  -l: download location (default: /tmp)"
  echo "  -v: version (e.g. 1.0.0)"
  exit 1
}

distro=""
location="/tmp"

while getopts ":drl:v:" opt; do
  case $opt in
    d)
      if [ -n "$distro" ]; then
        usage
      fi
      distro="debian"
      ;;
    r)
      if [ -n "$distro" ]; then
        usage
      fi
      distro="redhat"
      ;;
    l)
      location="$OPTARG"
      ;;
    v)
      version_regex="^[0-9]+\.[0-9]+\.[0-9]+$"
      if ! [[ "$OPTARG" =~ $version_regex ]]; then
        usage
      fi
      version="$OPTARG"
      major_version="${version%%.*}"
      minor_version="${version#*.}"
      minor_version="${minor_version%%.*}"
      release_version="${version##*.}"
      if [ "$distro" == "debian" ]; then
        cassandra_url="https://archive.apache.org/dist/cassandra/debian/pool/main/c/cassandra/cassandra_${version}_all.deb"
        cassandra_tools_url="https://archive.apache.org/dist/cassandra/debian/pool/main/c/cassandra/cassandra-tools_${version}_all.deb"
      else
        url_version="${major_version}${minor_version}x"
        cassandra_url="https://archive.apache.org/dist/cassandra/redhat/${url_version}/cassandra-$version-1.noarch.rpm"
        cassandra_tools_url="https://archive.apache.org/dist/cassandra/redhat/${url_version}/cassandra-tools-$version-1.noarch.rpm"
      fi
      ;;
    \?)
      usage
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage
      ;;
  esac
done

if [ -z "$distro" ]; then
  usage
fi

if [ "$distro" == "debian" ]; then
  echo "Selected distro: $distro"
  echo "Version: $version"
  echo "Downloading Cassandra from $cassandra_url"
  curl -L $cassandra_url -o "$location/cassandra_${version}_all.deb"
  echo "Downloading Cassandra Tools from $cassandra_tools_url"
  curl -L $cassandra_tools_url -o "$location/cassandra-tools_${version}_all.deb"
else
  echo "Selected distro: $distro"
  echo "Version: $version"
  echo "Downloading Cassandra from $cassandra_url"
  curl -L $cassandra_url -o "$location/cassandra-$version-1.noarch.rpm"
  echo "Downloading Cassandra Tools from $cassandra_tools_url"
  curl -L $cassandra_tools_url -o "$location/cassandra-tools-$version-1.noarch.rpm"
fi
