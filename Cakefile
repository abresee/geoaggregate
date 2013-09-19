fs = require 'fs'

{print} = require 'sys'
{spawn} = require 'child_process'

build = (callback) ->
    src = 'tiger/coffee'
    build = 'tiger/static/tiger/scripts'
    coffee = spawn 'coffee', ['-c', '-o', build, src]
    coffee.stderr.on 'data', (data) ->
        process.stderr.write data.toString()
    coffee.stdout.on 'data', (data) ->
        print data.tostring()
    coffee.on 'exit', (code) ->
        callback?() if code is 0

task 'tiger', 'build', ->
    build()
