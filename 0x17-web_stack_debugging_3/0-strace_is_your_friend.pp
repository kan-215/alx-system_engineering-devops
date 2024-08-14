# find out why Apache is returning a 500 error. 
# Once the issue is found, fix it and then automate it using Puppet

exec {'typing error':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
