FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/OllamaMcpServer/OllamaMcpServer.csproj src/OllamaMcpServer/
RUN dotnet restore src/OllamaMcpServer/OllamaMcpServer.csproj
COPY src/OllamaMcpServer/ src/OllamaMcpServer/
RUN dotnet publish src/OllamaMcpServer/OllamaMcpServer.csproj -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish ./
COPY rag-documents.json ./rag-documents.json
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "OllamaMcpServer.dll"]
