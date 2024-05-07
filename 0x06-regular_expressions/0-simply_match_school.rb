#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression match

puts ARGV[0].scan(/schoo/).join
