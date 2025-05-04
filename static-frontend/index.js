// index.js
document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
  
    try {
      const response = await fetch("http://127.0.0.1:8000/api/auth/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });
  
      console.log("Status:", response.status, response.statusText);
      const text = await response.text();
      console.log("Raw response text:", text);
  
      let data;
      try {
        data = JSON.parse(text);
      } catch {
        alert("Error: la respuesta no es JSON. Revisa la URL y CORS.");
        return;
      }
      console.log("Parsed JSON:", data);
  
      if (response.ok && data.token) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("role", data.role || "");
        window.location.href = "dashboard.html";
        // No guardamos aquí: redirigimos al ifn_service pasándole token y role
        const params = new URLSearchParams({
         token: data.token,
         role: data.role || ""
        });
        window.location.href =
            "http://127.0.0.1:8001/dashboard/?" + params.toString();
      } else {
        alert("Credenciales inválidas:\n" + (data.detail || JSON.stringify(data)));
      }
    } catch (err) {
      console.error("Fetch error:", err);
      alert("No se pudo conectar al servidor de login.");
    }
  });
  