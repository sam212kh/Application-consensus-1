import axios from "axios";
import EventBus from "../event-bus";

axios.interceptors.response.use(
  function(response) {
    return response;
  },
  function(error) {
    if (401 === error.response.status) {
      EventBus.$emit("user:session-expired");
    }
    return Promise.reject(error);
  }
);

export default axios.create({
  baseURL: "/api/v1",
  timeout: 5000,
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json"
  }
});
