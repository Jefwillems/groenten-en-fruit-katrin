(() => {
  window.stateSync = {
    init(collection) {
      this.isInitialized = true;
      this.collection = collection;
      this.state = JSON.parse(localStorage.getItem(collection)) || {};
    },
    setValue(key, value) {
      this.checkInit();
      this.state[key] = value;
      this.saveState();
    },
    getValue(key) {
      this.checkInit();
      return this.state[key];
    },
    reset() {
      this.state = {};
      this.saveState();
    },
    saveState() {
      this.checkInit();
      localStorage.setItem(this.collection, JSON.stringify(this.state))
    },
    checkInit() {
      if (!this.isInitialized) throw new Error("State was not initialized");
    }
  }
})();


