<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miro Board Incorporado</title>
    <!-- Carrega o Tailwind CSS para estilização -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Define a fonte Inter para todo o corpo da página */
        body {
            font-family: "Inter", sans-serif;
        }
        /* Estilos para o contêiner do iframe */
        .iframe-container {
            position: relative;
            width: 100%;
            /* Proporção 16:9 para o iframe */
            padding-bottom: 56.25%; /* 9 / 16 * 100 */
            height: 0;
            overflow: hidden;
            border-radius: 0.75rem; /* cantos arredondados */
        }
        .iframe-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
            border-radius: 0.75rem; /* cantos arredondados */
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
    <div class="w-full max-w-4xl bg-white rounded-xl shadow-lg p-6">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-6 rounded-md p-2">
            Seu Quadro Miro
        </h1>
        <div class="iframe-container">
            <!-- O iframe incorpora o Miro board -->
            <iframe
                src="https://miro.com/app/live-embed/uXjVJe6xKUk=/?embedMode=view_only_without_ui&moveToViewport=44424,21362,45174,69873&embedId=267193006703"
                frameborder="0"
                scrolling="no"
                allow="fullscreen; clipboard-read; clipboard-write"
                allowfullscreen
            ></iframe>
        </div>
        <p class="text-center text-gray-600 mt-6">
            Este é o seu quadro Miro incorporado. Você pode interagir com ele diretamente aqui.
        </p>
    </div>
</body>
</html>
