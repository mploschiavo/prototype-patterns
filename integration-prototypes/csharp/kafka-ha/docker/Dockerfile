FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/KafkaHaClients/KafkaHaClients.csproj src/KafkaHaClients/
RUN dotnet restore src/KafkaHaClients/KafkaHaClients.csproj
COPY src/KafkaHaClients/ src/KafkaHaClients/
RUN dotnet publish src/KafkaHaClients/KafkaHaClients.csproj -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/runtime:8.0
WORKDIR /app
COPY --from=build /app/publish ./
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENV KAFKA_CLIENT_MODE=producer
ENV CSHARP_DLL=KafkaHaClients.dll
ENTRYPOINT ["/entrypoint.sh"]
