async function predictRisk() {
    try {

        const age = Number(document.getElementById("age").value);
        const income = Number(document.getElementById("income").value);
        const education = Number(document.getElementById("education").value);
        const experience = Number(document.getElementById("experience").value);
        const credit = Number(document.getElementById("credit").value);

        const data = [
            age,
            income,
            education,
            experience,
            credit,

            income * 0.25,      // loan_amount
            36,                 // duration
            credit < 500 ? 18 : 8,
            income < 25000 ? 0.8 : 0.25,
            income * 0.3,
            income * 0.2,
            income * 0.1,
            age < 25 ? 4 : 2,
            experience,
            credit > 700 ? 8 : 4,
            age > 30 ? 7 : 4,
            credit < 500 ? 8 : 3,
            credit > 700 ? 9 : 4,
            credit < 500 ? 8 : 5,
            6,
            5,
            credit < 500 ? 8 : 3,
            credit < 500 ? 4 : 0,
            education > 14 ? 8 : 3
        ];

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("result").innerText =
            result.prediction;

    } catch (error) {
        console.error(error);
        document.getElementById("result").innerText =
            "Error";
    }
}