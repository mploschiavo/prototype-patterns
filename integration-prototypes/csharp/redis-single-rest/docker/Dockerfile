FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/RedisSingleRestService/RedisSingleRestService.csproj src/RedisSingleRestService/
RUN dotnet restore src/RedisSingleRestService/RedisSingleRestService.csproj
COPY src/RedisSingleRestService/ src/RedisSingleRestService/
RUN dotnet publish src/RedisSingleRestService/RedisSingleRestService.csproj -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish ./
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "RedisSingleRestService.dll"]
