document.addEventListener("DOMContentLoaded", () =>
{
    const form = document.querySelector("form");
    const site = document.querySelector("input[name='url']");

    form.addEventListener("submit", (event) => 
    {
        const url = site.value.trim();

        if (!isValidUrl(url))
        {
            event.preventDefault();
            alert("Por favor, digite uma URL válida (ex: https://google.com)");
        }
    });
});


function isValidUrl(string)
{
    try
    {
        new URL(string);
        return true;
    }
    catch (_)
    {
        return false;
    }
}