(() => {
  const validateAndAdjust = (x) => x >= 0 ? x : 0;
  const addOne = (x) => x + 1;
  const substractOne = (x) => x - 1;

  const createNewValue = (target, fn) => {
    const currentValue = parseInt(target.innerText, 10);
    const newValue = fn(currentValue);
    return validateAndAdjust(newValue)
  };

  class App {
    constructor() {
      this.addBtns = document.querySelectorAll('.add-item');
      this.removeBtns = document.querySelectorAll('.remove-item');
      stateSync.init('order_form')
    }

    init() {
      this.setupButtons(this.addBtns, addOne);
      this.setupButtons(this.removeBtns, substractOne)
    }

    setupButtons(btns, fn) {
      [].forEach.call(btns, (btn) => {
        btn.addEventListener('click', (ev) => {
          const targetNode = ev.target.parentNode.children[1];
          const newValue = createNewValue(targetNode, fn);
          targetNode.innerText = newValue;
          stateSync.setValue(targetNode.id, newValue);
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