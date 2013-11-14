# puppet manifest

Exec {
    path => [
    '/usr/local/sbin',
    '/usr/local/bin',
    '/usr/sbin',
    '/usr/bin',
    '/sbin',
    '/bin',
    ],
    logoutput => true,
}

exec {'apt-get-update':
    command => 'apt-get update'
}

# make sure we have some basic tools and libraries available

package {'libxslt1-dev':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'build-essential':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'python-dev':
    ensure => installed,
    require => Exec['apt-get-update']
}

package {'python-pip':
    ensure => installed,
    require => Package['python-dev']
}

package {'libaio1':
    ensure => installed,
    require => Exec['apt-get-update']
}

package {'libaio-dev':
    ensure => installed,
    require => Exec['apt-get-update']
}

package {'git':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'unzip':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'curl':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'wget':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'libcurl4-openssl-dev':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'openssl':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'zlib1g-dev':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'libsqlite3-dev':
    ensure => latest,
    require => Exec['apt-get-update'],
}

package {'sqlite3':
    ensure => latest,
    require => Exec['apt-get-update'],
}

# install virtualenv and virtualenvwrapper - depends on pip

package {'virtualenv':
    ensure => latest,
    provider => 'pip',
    require => [ Package['python-pip'], ],
}

package {'virtualenvwrapper':
    ensure => latest,
    provider => 'pip',
    require => [ Package['python-pip'], ],
}

file {'/etc/profile.d/venvwrapper.sh':
    ensure => file,
    content => 'source `which virtualenvwrapper.sh`',
    mode => '755',
    require => Package['virtualenvwrapper'],
}

# install the Oracle instant client

define download ($uri, $timeout = 300) {
  exec {
      "download $uri":
          command => "wget -q '$uri' -O $name",
          creates => $name,
          timeout => $timeout,
          require => Package['wget'],
  }
}

download {
  "/tmp/instantclient-basiclite-linux.x64-11.2.0.3.0.zip":
      uri => "http://test.isites.harvard.edu/oracle/instantclient-basiclite-linux.x64-11.2.0.3.0.zip",
      timeout => 900;
}

download {
  "/tmp/instantclient-sqlplus-linux.x64-11.2.0.3.0.zip":
      uri => "http://test.isites.harvard.edu/oracle/instantclient-sqlplus-linux.x64-11.2.0.3.0.zip",
      timeout => 900;
}

download {
  "/tmp/instantclient-sdk-linux.x64-11.2.0.3.0.zip":
      uri => "http://test.isites.harvard.edu/oracle/instantclient-sdk-linux.x64-11.2.0.3.0.zip",
      timeout => 900;
}

file {'/opt/oracle':
    ensure => directory,
}

exec {'instantclient-basiclite':
    require => [ Download['/tmp/instantclient-basiclite-linux.x64-11.2.0.3.0.zip'], File['/opt/oracle'], Package['unzip'] ],
    cwd => '/opt/oracle',
    command => 'unzip /vagrant/vagrant/files/instantclient-basiclite-linux.x64-11.2.0.3.0.zip',
    creates => '/opt/oracle/instantclient_11_2/BASIC_LITE_README',
}

exec {'instantclient-sqlplus':
    require => [ Download['/tmp/instantclient-sqlplus-linux.x64-11.2.0.3.0.zip'], File['/opt/oracle'], Package['unzip'] ],
    cwd => '/opt/oracle',
    command => 'unzip /vagrant/vagrant/files/instantclient-sqlplus-linux.x64-11.2.0.3.0.zip',
    creates => '/opt/oracle/instantclient_11_2/sqlplus',
}

exec {'instantclient-sdk':
    require => [ Download['/tmp/instantclient-sdk-linux.x64-11.2.0.3.0.zip'], File['/opt/oracle'], Package['unzip'] ],
    cwd => '/opt/oracle',
    command => 'unzip /vagrant/vagrant/files/instantclient-sdk-linux.x64-11.2.0.3.0.zip',
    creates => '/opt/oracle/instantclient_11_2/sdk',
}

file {'/opt/oracle/instantclient_11_2/libclntsh.so':
    ensure => link,
    target => 'libclntsh.so.11.1',
    require => Exec['instantclient-basiclite'],
}

file {'/opt/oracle/instantclient_11_2/libocci.so':
    ensure => link,
    target => 'libocci.so.11.1',
    require => Exec['instantclient-basiclite'],
}

file {'/etc/profile.d/oracle.sh':
    ensure => file,
    content => 'export ORACLE_HOME=/opt/oracle/instantclient_11_2; export PATH=$ORACLE_HOME:$PATH; export LD_LIBRARY_PATH=$ORACLE_HOME',
    mode => '755',
    require => Exec['instantclient-basiclite'],
}



