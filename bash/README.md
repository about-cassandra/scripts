## Cassandra Download Script

This is a Bash script that downloads the Cassandra and Cassandra Tools packages for either the `debian` or `redhat` distros, based on the specified version.

### Usage

`./cassandra_download.sh [-d|-r] -v <version> [-l <location>]`


#### Options

- `-d`: Selects the `debian` distro.
- `-r`: Selects the `redhat` distro.
- `-v <version>`: Specifies the version to download in the format `major.minor.release`, e.g. `3.11.10`.
- `-l <location>`: Specifies the location to download the packages to. Default is `/tmp`.

### Example Usage

Download Cassandra and Cassandra Tools RPMs for redhat:

`./cassandra_download.sh -r -v 3.11.10 -l /home/user/downloads`


Download Cassandra and Cassandra Tools DEB packages for debian:


`./cassandra_download.sh -d -v 3.11.10 -l /home/user/downloads`

### Notes

- If the `-d` option is used, the script will download the Cassandra and Cassandra Tools DEB packages for the specified version. Otherwise, it will download the RPM packages for redhat.
- This script uses the `curl` command to download the packages. If `curl` is not installed, the script will not work properly.

### License

This script is licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an **"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND**, either express or implied. See the License for the specific language governing permissions and limitations under the License.