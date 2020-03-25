# Change the configuration file of ssh

# Change password authentication
file_line { 'ssh_config no pass':
  ensure   => 'present',
  path     => '/etc/ssh/ssh_config',
  line     => '#   PasswordAuthentication no',
  match    => '#   PasswordAuthentication'
}

# Adds
file_line { 'ssh_config add key':
  ensure   => 'present',
  path     => '/etc/ssh/ssh_config',
  line     => '#   IdentityFile ~/.ssh/holberton',
  match    => '#   IdentityFile ~/.ssh/holberton'
}
