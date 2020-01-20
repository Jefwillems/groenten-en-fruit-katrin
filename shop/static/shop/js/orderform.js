(() => {
  const validateAndAdjust = (x) => x >= 0 ? x : 0;
  const addOne = (x) => x + 1;
  const substractOne = (x) => x - 1;

  const createNewValue = (target, fn) => {
    const currentValue = parseInt(target.innerText, 10);
    const newValue = fn(currentValue);
    target.innerText = validateAndAdjust(newValue)
  };

  class App {
    constructor() {
      this.addBtns = document.querySelectorAll('.add-item');
      this.removeBtns = document.querySelectorAll('.remove-item');
    }

    init() {
      [].forEach.call(this.addBtns, (btn) => {
        btn.addEventListener('click', (ev) => {
          createNewValue(ev.target.parentNode.children[1], addOne)
        })
      });

      [].forEach.call(this.removeBtns, (btn) => {
        btn.addEventListener('click', (ev) => {
          createNewValue(ev.target.parentNode.children[1], substractOne)
        });
      });
    }
  }

  let app;

  document.addEventListener('DOMContentLoaded', () => {
    app = new App();
    app.init();
  }, false)
})();