// Generated by CoffeeScript 1.4.0
(function() {
  var ListCtrller,
    __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  ListCtrller = (function(_super) {

    __extends(ListCtrller, _super);

    function ListCtrller() {
      return ListCtrller.__super__.constructor.apply(this, arguments);
    }

    ListCtrller.prototype.events = {
      "tap li": "showLista"
    };

    ListCtrller.prototype.showLista = function(event) {
      console.log(event);
      return alert("yeaahh!!!");
    };

    return ListCtrller;

  })(Monocle.Controller);

  __Controller.NewList = new ListCtrller("article#myList");

}).call(this);
