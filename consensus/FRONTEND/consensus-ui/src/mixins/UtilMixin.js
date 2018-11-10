import $ from "jquery";
import moment from "moment";

require("animate.css");
require("bootstrap4-notify");

export default {
  methods: {
    formatDate: function(value, fmt, _default) {
      _default = _default === undefined ? "" : _default;
      if (!value) {
        return _default;
      }
      fmt = fmt === undefined ? "MMM D, YYYY HH:mm" : fmt;
      return moment(value).format(fmt);
    },
    capitalize: function(value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    },
    findIndexBy: function(array, property, value) {
      for (let i = 0; i < array.length; i++) {
        if (array[i][property] === value) {
          return i;
        }
      }
      return -1;
    },
    findValueBy: function(array, property, value) {
      for (let i = 0; i < array.length; i++) {
        if (array[i][property] === value) {
          return array[i];
        }
      }
    },
    closeAllNotify: function() {
      $.notifyClose();
    },
    notifyMessage: function(msgOptions, settings) {
      settings = Object.assign(
        {
          element: "body", // which element to append to
          type: "info", // (null, 'info', 'danger', 'success')
          newest_on_top: true,
          width: "auto", // (integer, or 'auto')
          timer: 5000, // Time while the message will be displayed. It's not equivalent to the *demo* timeOut!
          z_index: 9999999,
          allow_dismiss: true // If true then will display a cross to close the popup.
        },
        settings || {}
      );
      if (typeof msgOptions === "string") {
        msgOptions = { message: msgOptions };
      }
      $.notify(msgOptions, settings);
    },
    notifySuccess: function(msg, delay) {
      this.notifyMessage(msg, {
        type: "success",
        timer: delay !== undefined ? delay : 5000
      });
    },
    notifyError: function(msg, delay) {
      this.notifyMessage(msg, {
        type: "danger",
        timer: delay !== undefined ? delay : 5000
      });
    },
    notifyWarn: function(msg, delay) {
      this.notifyMessage(msg, {
        type: "warning",
        timer: delay !== undefined ? delay : 5000
      });
    },
    notifyInfo: function(msg, delay) {
      this.notifyMessage(msg, {
        type: "info",
        timer: delay !== undefined ? delay : 5000
      });
    },
    notifyDefaultServerSuccess: function(response, delay) {
      delay = delay !== undefined ? delay : 5000;
      let defaultMsg = "Operation done successfully";
      this.notifySuccess(response.statusText || defaultMsg, delay);
    },
    notifyDefaultServerError: function(
      error,
      showDetails,
      delay,
      extra_message
    ) {
      let response = error.response || error.request;
      if (response.status === 401) {
        return;
      }
      let msg;
      delay = delay !== undefined ? delay : 5000;
      showDetails = showDetails !== undefined ? showDetails : true;
      if (!response || response.status <= 0) {
        msg = "<strong>Server Connection Error</strong>";
      } else {
        msg =
          "<strong>" +
          response.status +
          ": " +
          response.statusText +
          "</strong>";
        let jData = this.safeJsonParse(response.data);
        if (showDetails && jData) {
          msg += "<p>" + this.prettifyError(response.data) + "</p>";
        }
        if (extra_message) {
          msg += "<p>" + extra_message + "</p>";
        }
      }
      this.notifyError(msg, delay);
    },
    prettifyError: function(data) {
      return JSON.stringify(data)
        .replace(/\[|\]|\}|\{/g, "")
        .replace(/\\"/g, '"')
        .replace('"non_field_errors":', "");
    },
    safeJsonParse: function(s, nullIfFail) {
      if (typeof s === "object") {
        return s;
      }
      nullIfFail = nullIfFail === undefined;
      try {
        return JSON.parse(s);
      } catch (e) {
        return nullIfFail ? null : s;
      }
    },
    randomId: function(n) {
      n = n || 10;
      return Math.floor(Math.random() * Math.pow(10, n) + 1);
    },
    addQSParm: function(url, name, value, override) {
      override = override === undefined ? true : override;
      let self = this;
      if (value instanceof Array) {
        $.each(value, function(k, v) {
          url = self.addQSParm(url, name, v, false);
        });
        return url;
      }
      let re = new RegExp("([?&]" + name + "=)[^&]+", "");

      function add(sep) {
        url += sep + name + "=" + encodeURIComponent(value);
      }

      function change() {
        url = url.replace(re, "$1" + encodeURIComponent(value));
      }

      if (url.indexOf("?") === -1) {
        add("?");
      } else {
        if (override && re.test(url)) {
          change();
        } else {
          add("&");
        }
      }
      return url;
    },
    noCacheUrl: function(url) {
      let r = this.randomId();
      return this.addQSParm(url, "nc", r);
    },
    combineURLs: function(baseURL, relativeURL) {
      return (
        baseURL.replace(/\/+$/, "") + "/" + relativeURL.replace(/^\/+/, "")
      );
    }
  }
};
