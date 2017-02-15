class Person {
    protected name:string = "Joe";
    protected age:number = 17;

    describe(): string {
        return this.name + this.age
    }
}

class Philip extends Person {
    name = "Philip";

    constructor(age:number) {
        super();
        this.age = age;
    }
}

let joe = new Person();
let phil = new Philip(26.6);

document.write("Hello WORLD!");
document.write(joe.describe());
document.write(phil.describe());