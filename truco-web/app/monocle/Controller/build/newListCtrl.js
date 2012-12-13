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
      "tap a[data-action=cancell]": "cancelled",
      "tap a[data-action=saveList]": "saved"
    };

    ListCtrller.prototype.cancelled = function(event) {
      Lungo.Router.back();
      return Lungo.Notification.alert("Error", "Cancelaste la creación", "warning", 7);
    };

    ListCtrller.prototype.saved = function(event) {
      return Lungo.Notification.success("Success", "Successful operation", "check", 7);
    };

    return ListCtrller;

  })(Monocle.Controller);

  __Controller.createList = new ListCtrller("section#list_detail");

}).call(this);
