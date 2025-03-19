const userAgent = navigator.userAgent;

if (userAgent.includes("Edg")) { // Edge
    alert("You've got the Edge!");
} else if (userAgent.includes("Chrome") || userAgent.includes("Firefox") || userAgent.includes("Safari") || userAgent.includes("Opera")) {
    alert("Okay we support these browsers too");
} else {
    alert("We hope that this page looks ok!");
}
