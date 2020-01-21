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
      this.valueElems = document.querySelectorAll("[id^='amount-']");
      this.form = document.getElementById('order-form');
      stateSync.init('order_form')
    }

    init() {
      this.setupButtons(this.addBtns, addOne);
      this.setupButtons(this.removeBtns, substractOne);
      this.setupStoredValues();
      this.hookForm();
    }

    setupStoredValues() {
      [].forEach.call(this.valueElems, (valueElem) => {
        valueElem.innerText = stateSync.getValue(valueElem.id) || 0;
      });
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

    hookForm() {
      this.form.addEventListener('submit', (ev) => {
        Object.entries(stateSync.state).map(([key, value]) => {
          const input = document.createElement('input');
          input.hidden = true;
          input.name = key;
          input.value = value;
          return input;
        }).forEach(element => {
          this.form.appendChild(element);
        });
        stateSync.reset();
        return true;
      })
    }
  }

  let app;

  document.addEventListener('DOMContentLoaded', () => {
    app = new App();
    app.init();
  }, false)
})();