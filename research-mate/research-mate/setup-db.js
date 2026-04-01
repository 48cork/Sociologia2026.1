const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

// O banco será criado aqui nesta pasta
const db = new sqlite3.Database('./researchmate.db');

// Buscamos o SQL que está na pasta pai
try {
    const sql = fs.readFileSync('../schema.sql').toString();
    db.serialize(() => {
        db.exec(sql, (err) => {
            if (err) { console.error("❌ Erro no SQL:", err.message); }
            else { console.log("✅ ResearchMate: Banco de dados de Sociologia criado com sucesso!"); }
        });
    });
} catch (e) {
    console.error("❌ Erro: O arquivo schema.sql não foi encontrado na pasta anterior.");
}
db.close();
