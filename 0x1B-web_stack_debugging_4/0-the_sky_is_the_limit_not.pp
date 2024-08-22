# Puppet script to fix request dropping in Nginx by increasing ulimit and restarting Nginx

# Increase the maximum number of file descriptors (ulimit) for Nginx
exec { 'increase ulimit':
  path    => '/bin',
  command => "sed -i 's/15/2000/g' /etc/default/nginx",
  onlyif  => "grep -q 'ulimit -n 15' /etc/default/nginx",
  notify  => Exec['nginx restart'],  # Triggers a restart after change
}

# Restart Nginx to apply changes
exec { 'nginx restart':
  path    => '/usr/sbin',
  command => 'service nginx restart',
  refreshonly => true,  # Restart only when triggered
}
