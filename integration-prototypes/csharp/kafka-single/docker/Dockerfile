FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/KafkaSingleClients/KafkaSingleClients.csproj src/KafkaSingleClients/
RUN dotnet restore src/KafkaSingleClients/KafkaSingleClients.csproj
COPY src/KafkaSingleClients/ src/KafkaSingleClients/
RUN dotnet publish src/KafkaSingleClients/KafkaSingleClients.csproj -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/runtime:8.0
WORKDIR /app
COPY --from=build /app/publish ./
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENV KAFKA_CLIENT_MODE=producer
ENV CSHARP_DLL=KafkaSingleClients.dll
ENTRYPOINT ["/entrypoint.sh"]
