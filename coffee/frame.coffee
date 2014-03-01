###
$->
    documnt ready body
###
class Map

    constructor: ->
        @obj = new Object()
    put: (key,value) ->
        @obj[key] - value
        return @
    get: (key) ->
        return @obj[key]
    remove: (key) ->
        delete @obj[key] if get(key)?
        return @
    contains: (key) ->
        return get(key)?
    clear: ->
        @obj = new Object()
    size: ->
        return @obj.keys().length
    keys: ->
        arr = new Array()
        for tem in @obj
            do arr.push tem
        return arr
    values: ->
        arr = new Array()
        for tem in @obj
            do arr.push @obj[tem]
        return arr


class Tomatodo
    ready: ->


class Frame
    addTab: (tab)->
        @allTab.append tab

    ready: ->
        


class Tab
    constructor:(@id,@name,@url) ->

    fetch : ->
        

    show: ->
        fetch if not @content?

$ ->
    t = new Tomatodo 
    t.sayHello "y"