window.addEventListener('DOMContentLoaded', (event) => {
    const inputs = document.querySelectorAll("input, select");
    for (let i = 0; i < inputs.length; i++) {
        inputs[i].classList.add("block", "w-full", "border", "border-gray-200", "rounded-md", "py-4", "px-4", "mt-3", "focus:border-blue-400", "focus:ring-blue-300", "focus:ring", "focus:outline-none", "focus:ring-opacity-30");
    }
});