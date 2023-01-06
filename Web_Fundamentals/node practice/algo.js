function d6() {
    var diceroll = Math.random();
    if (diceroll == 0) {
        diceroll = 1;
    } else {
        diceroll = Math.ceil(diceroll * 6)
    }
    console.log(diceroll);
}
d6();