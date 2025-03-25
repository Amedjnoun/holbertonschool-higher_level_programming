export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Species = Symbol('species');
    return new (this.constructor[Species] || this.constructor)();
  }

  static get [Symbol.species]() {
    return this;
  }
}
