namespace PrototypePatterns.Structural.Facade;

public sealed class Lights
{
    public string Dim() => "lights dimmed";
}

public sealed class Projector
{
    public string On() => "projector on";
}

public sealed class SoundSystem
{
    public string Surround() => "surround enabled";
}

public sealed class HomeTheaterFacade(Lights lights, Projector projector, SoundSystem soundSystem)
{
    public string WatchMovie() => $"{lights.Dim()} | {projector.On()} | {soundSystem.Surround()}";
}

public static class FacadePattern
{
    public static string Demo() => new HomeTheaterFacade(new Lights(), new Projector(), new SoundSystem()).WatchMovie();
}
