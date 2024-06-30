# Configure SSH client settings using Puppet
# Ensure connection to server without typing a password

include stdlib

# Define the SSH config file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Ensure the IdentityFile is set to ~/.ssh/school
file_line { 'Set SSH Private Key':
  path    => $ssh_config_file,
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^\s*IdentityFile\s+~/.ssh/.*$',
  ensure  => present,
  after   => '# Host-specific definitions',
}

# Ensure PasswordAuthentication is disabled
file_line { 'Disable Password Auth':
  path    => $ssh_config_file,
  line    => '    PasswordAuthentication no',
  match   => '^\s*PasswordAuthentication\s+(yes|no)$',
  ensure  => present,
  after   => '# Host-specific definitions',
}

# Explanation of Regex Patterns:
#
# ^\s*                      - Matches the beginning of the line followed by any whitespace
# IdentityFile\s+           - Matches the literal "IdentityFile" followed by at least one whitespace
# ~/.ssh/.*$                - Matches any path starting with ~/.ssh/ and any characters until the end of the line
#
# ^\s*                      - Matches the beginning of the line followed by any whitespace
# PasswordAuthentication\s+ - Matches the literal "PasswordAuthentication" followed by at least one whitespace
# (yes|no)$                 - Matches either "yes" or "no" until the end of the line
