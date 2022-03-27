"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/api/payment_intents";
exports.ids = ["pages/api/payment_intents"];
exports.modules = {

/***/ "stripe":
/*!*************************!*\
  !*** external "stripe" ***!
  \*************************/
/***/ ((module) => {

module.exports = require("stripe");

/***/ }),

/***/ "(api)/./pages/api/payment_intents.js":
/*!**************************************!*\
  !*** ./pages/api/payment_intents.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var stripe__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! stripe */ \"stripe\");\n/* harmony import */ var stripe__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(stripe__WEBPACK_IMPORTED_MODULE_0__);\n\nconst stripe = new (stripe__WEBPACK_IMPORTED_MODULE_0___default())(process.env.SECRET_KEY);\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (async (req, res)=>{\n    if (req.method === \"POST\") {\n        try {\n            const { amount  } = req.body;\n            // Psst. For production-ready applications we recommend not using the\n            // amount directly from the client without verifying it first. This is to\n            // prevent bad actors from changing the total amount on the client before\n            // it gets sent to the server. A good approach is to send the quantity of\n            // a uniquely identifiable product and calculate the total price server-side.\n            // Then, you would only fulfill orders using the quantity you charged for.\n            const paymentIntent = await stripe.paymentIntents.create({\n                amount,\n                currency: \"usd\"\n            });\n            res.status(200).send(paymentIntent.client_secret);\n        } catch (err) {\n            res.status(500).json({\n                statusCode: 500,\n                message: err.message\n            });\n        }\n    } else {\n        res.setHeader(\"Allow\", \"POST\");\n        res.status(405).end(\"Method Not Allowed\");\n    }\n});\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwaSkvLi9wYWdlcy9hcGkvcGF5bWVudF9pbnRlbnRzLmpzLmpzIiwibWFwcGluZ3MiOiI7Ozs7OztBQUEyQjtBQUUzQixLQUFLLENBQUNDLE1BQU0sR0FBRyxHQUFHLENBQUNELCtDQUFNLENBQUNFLE9BQU8sQ0FBQ0MsR0FBRyxDQUFDQyxVQUFVO0FBRWhELGlFQUFNLE9BQWdCQyxHQUFHLEVBQUVDLEdBQUcsR0FBSyxDQUFDO0lBQ2xDLEVBQUUsRUFBRUQsR0FBRyxDQUFDRSxNQUFNLEtBQUssQ0FBTSxPQUFFLENBQUM7UUFDMUIsR0FBRyxDQUFDLENBQUM7WUFDSCxLQUFLLENBQUMsQ0FBQyxDQUFDQyxNQUFNLEVBQUMsQ0FBQyxHQUFHSCxHQUFHLENBQUNJLElBQUk7WUFDM0IsRUFBcUU7WUFDckUsRUFBeUU7WUFDekUsRUFBeUU7WUFDekUsRUFBeUU7WUFDekUsRUFBNkU7WUFDN0UsRUFBMEU7WUFFMUUsS0FBSyxDQUFDQyxhQUFhLEdBQUcsS0FBSyxDQUFDVCxNQUFNLENBQUNVLGNBQWMsQ0FBQ0MsTUFBTSxDQUFDLENBQUM7Z0JBQ3hESixNQUFNO2dCQUNOSyxRQUFRLEVBQUUsQ0FBSztZQUNqQixDQUFDO1lBRURQLEdBQUcsQ0FBQ1EsTUFBTSxDQUFDLEdBQUcsRUFBRUMsSUFBSSxDQUFDTCxhQUFhLENBQUNNLGFBQWEsQ0FBQyxDQUFDO1FBQ3BELENBQUMsQ0FBQyxLQUFLLEVBQUVDLEdBQUcsRUFBRSxDQUFDO1lBQ2JYLEdBQUcsQ0FBQ1EsTUFBTSxDQUFDLEdBQUcsRUFBRUksSUFBSSxDQUFDLENBQUM7Z0JBQUNDLFVBQVUsRUFBRSxHQUFHO2dCQUFFQyxPQUFPLEVBQUVILEdBQUcsQ0FBQ0csT0FBTztZQUFDLENBQUMsQ0FBQyxDQUFDO1FBQ2xFLENBQUM7SUFDSCxDQUFDLE1BQU0sQ0FBQztRQUNOZCxHQUFHLENBQUNlLFNBQVMsQ0FBQyxDQUFPLFFBQUUsQ0FBTSxNQUFDLENBQUM7UUFDL0JmLEdBQUcsQ0FBQ1EsTUFBTSxDQUFDLEdBQUcsRUFBRVEsR0FBRyxDQUFDLENBQW9CLG9CQUFDLENBQUM7SUFDNUMsQ0FBQztBQUNILENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9kb251dC1zaG9wLy4vcGFnZXMvYXBpL3BheW1lbnRfaW50ZW50cy5qcz9lZDBhIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCBTdHJpcGUgZnJvbSBcInN0cmlwZVwiO1xuXG5jb25zdCBzdHJpcGUgPSBuZXcgU3RyaXBlKHByb2Nlc3MuZW52LlNFQ1JFVF9LRVkpO1xuXG5leHBvcnQgZGVmYXVsdCBhc3luYyAocmVxLCByZXMpID0+IHtcbiAgaWYgKHJlcS5tZXRob2QgPT09IFwiUE9TVFwiKSB7XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IHsgYW1vdW50IH0gPSByZXEuYm9keTtcbiAgICAgIC8vIFBzc3QuIEZvciBwcm9kdWN0aW9uLXJlYWR5IGFwcGxpY2F0aW9ucyB3ZSByZWNvbW1lbmQgbm90IHVzaW5nIHRoZVxuICAgICAgLy8gYW1vdW50IGRpcmVjdGx5IGZyb20gdGhlIGNsaWVudCB3aXRob3V0IHZlcmlmeWluZyBpdCBmaXJzdC4gVGhpcyBpcyB0b1xuICAgICAgLy8gcHJldmVudCBiYWQgYWN0b3JzIGZyb20gY2hhbmdpbmcgdGhlIHRvdGFsIGFtb3VudCBvbiB0aGUgY2xpZW50IGJlZm9yZVxuICAgICAgLy8gaXQgZ2V0cyBzZW50IHRvIHRoZSBzZXJ2ZXIuIEEgZ29vZCBhcHByb2FjaCBpcyB0byBzZW5kIHRoZSBxdWFudGl0eSBvZlxuICAgICAgLy8gYSB1bmlxdWVseSBpZGVudGlmaWFibGUgcHJvZHVjdCBhbmQgY2FsY3VsYXRlIHRoZSB0b3RhbCBwcmljZSBzZXJ2ZXItc2lkZS5cbiAgICAgIC8vIFRoZW4sIHlvdSB3b3VsZCBvbmx5IGZ1bGZpbGwgb3JkZXJzIHVzaW5nIHRoZSBxdWFudGl0eSB5b3UgY2hhcmdlZCBmb3IuXG5cbiAgICAgIGNvbnN0IHBheW1lbnRJbnRlbnQgPSBhd2FpdCBzdHJpcGUucGF5bWVudEludGVudHMuY3JlYXRlKHtcbiAgICAgICAgYW1vdW50LFxuICAgICAgICBjdXJyZW5jeTogXCJ1c2RcIlxuICAgICAgfSk7XG5cbiAgICAgIHJlcy5zdGF0dXMoMjAwKS5zZW5kKHBheW1lbnRJbnRlbnQuY2xpZW50X3NlY3JldCk7XG4gICAgfSBjYXRjaCAoZXJyKSB7XG4gICAgICByZXMuc3RhdHVzKDUwMCkuanNvbih7IHN0YXR1c0NvZGU6IDUwMCwgbWVzc2FnZTogZXJyLm1lc3NhZ2UgfSk7XG4gICAgfVxuICB9IGVsc2Uge1xuICAgIHJlcy5zZXRIZWFkZXIoXCJBbGxvd1wiLCBcIlBPU1RcIik7XG4gICAgcmVzLnN0YXR1cyg0MDUpLmVuZChcIk1ldGhvZCBOb3QgQWxsb3dlZFwiKTtcbiAgfVxufTtcbiJdLCJuYW1lcyI6WyJTdHJpcGUiLCJzdHJpcGUiLCJwcm9jZXNzIiwiZW52IiwiU0VDUkVUX0tFWSIsInJlcSIsInJlcyIsIm1ldGhvZCIsImFtb3VudCIsImJvZHkiLCJwYXltZW50SW50ZW50IiwicGF5bWVudEludGVudHMiLCJjcmVhdGUiLCJjdXJyZW5jeSIsInN0YXR1cyIsInNlbmQiLCJjbGllbnRfc2VjcmV0IiwiZXJyIiwianNvbiIsInN0YXR1c0NvZGUiLCJtZXNzYWdlIiwic2V0SGVhZGVyIiwiZW5kIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(api)/./pages/api/payment_intents.js\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("(api)/./pages/api/payment_intents.js"));
module.exports = __webpack_exports__;

})();