var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
var nums = [];
function add() {
    var num = document.getElementById("num");
    var n1 = parseInt(num.value);
    if (isNaN(n1)) {
        alert("please enter the valid number");
        return;
    }
    nums.push(n1);
    (document.getElementById("list").textContent = nums.join(","));
    num.value = "";
}
function sort() {
    var sorted = __spreadArray([], nums, true).sort(function (a, b) { return a + b; });
    var dsort = __spreadArray([], nums, true).sort(function (a, b) { return b - a; });
    (document.getElementById("result").textContent = "sorted:".concat(sorted, " dsort:").concat(dsort));
}
