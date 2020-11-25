export default class Cat {
    constructor(id, score) {
        this.id = id;
        this.score = score;
    }

    static deserialize(serializedCat) {
        return new Cat(serializedCat.id, serializedCat.score);
    }
}