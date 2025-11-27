// Parameter
const lambda = 10;

// Poisson-Wahrscheinlichkeiten P(X=k) für k=0..20
const probs = [];
let pk = Math.exp(-lambda);   // P(0)
probs.push(pk);

// Rekursiv P(k+1) = P(k) * λ/(k+1)
for (let k = 0; k < 20; k++) {
    pk = pk * (lambda / (k + 1));
    probs.push(pk);
    console.log(probs[k]);
}

// P(X >= 20)
let sumTo19 = 0;
for (let k = 0; k < 20; k++) {
    sumTo19 += probs[k];
}
const p_ge20 = 1 - sumTo19;   // = P(X ≥ 20)


// Erwartungswert E[Y]
let EY = 0;
for (let k = 0; k < 20; k++) {
    EY += k * probs[k];
}
EY += 20 * p_ge20;   // abgeschnitten bei 20


// Erwartungswert von Y^2
let EY2 = 0;
for (let k = 0; k < 20; k++) {
    EY2 += k * k * probs[k];
}
EY2 += 400 * p_ge20;   // 20^2 * P(X ≥ 20)


// Varianz & Standardabweichung
const VY = EY2 - EY * EY;
const SDY = Math.sqrt(VY);

// Umsatzvariable U = 15 * Y
const EU = 15 * EY;
const SDU = 15 * SDY;


// Ausgabe
console.log("E[Y] =", EY);
console.log("V[Y] =", VY);
console.log("SD[Y] =", SDY);

console.log("Erwarteter Umsatz (E[U]) =", EU, "Euro");
console.log("Standardabweichung des Umsatzes =", SDU, "Euro");
